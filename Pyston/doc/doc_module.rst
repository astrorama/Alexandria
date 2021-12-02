Pyston
======

|Build Status|

Pyston is a “quick and dirty” C++ library that can be used to build
kind-of `AST <https://en.wikipedia.org/wiki/Abstract_syntax_tree>`__
leveraging the Python interpreter.

Problem statement
-----------------

SourceXtractor is configurable using a Python script. Some of the
parameters can be arbitrary functions that are evaluated at different
stages of the program: at the beginning, just at the beginning of the
model fitting, or inside the non-linear least squares loop.

However, Python is considerably less performant that C or C++ code
unless tooling like numpy (that perform most of the heavy lifting in C)
is used. The impact is particularly bad when running with multiple
threads, as everytime the program enters into the Python interpreter it
needs to acquire the `Global Interpreter
Lock <https://wiki.python.org/moin/GlobalInterpreterLock>`__, reducing
enormously the gain obtained by using multithreading.

Pyston aims to reduce this overhead building an AST only during the
first call, and forgetting about Python afterwards.

Mechanism
---------

The concept is in simple in principle:

In Python, as in C++, a developer can overload via methods, both
`logic <https://docs.python.org/3/reference/datamodel.html#basic-customization>`__
and
`mathematical <https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types>`__
operations.

As a quick example:

-  ``__add__`` overloads ``+``
-  ``__mul__`` overload ``*``
-  ``__ge__`` overloads ``>=``
-  …

This is how `numpy <https://numpy.org/>`__ or
`Keras <https://keras.io/>`__ can pull things like

.. code:: python

   a = np.random.rand(5, 20)
   b = np.random.rand(5, 20)
   x = a + b * 5 

Which is turned into

.. code:: python

   x = a.__add__(b.__mul__(5))

Of course, the return type does *not* have to be a number, it can be any
other object: for instance, operations over a numpy array return another
numpy array.

Knowing this, the idea is to evaluate a configured function, or lambda
expression, not with the actual values that need to be computed, but
with a kind of “Placeholder” object that triggers the building of the
AST.

For instance, imagine this expression:

.. code:: python

   f = lambda x, y: np.log(x) + y ** 2

If we call the lambda as this:

.. code:: python

   f(100, 5)

It isn’t hard to see how it would get evaluated, and f would return
``29.605``. However, as previously said, doing this inside the least
minimization loop is *very* expensive.

Imagine we call ``f``, however, with two of this “Placeholder” objects,
let’s call them ``px`` and ``py``

.. code:: python

   f(px, py)

Python itself will perform the evaluation, but calling the overloaded
methods, so we get something like

.. code:: python

   x.log().__add__(py.__pow__(2))

..

   **Note:** It turns out numpy will call a ``log`` method if the
   received type is unknown to it, and does so similarly for everything
   else, like ``sin``, ``exp``, etc…

Now, for instance ``py.__pow__(2)`` can return, instead of a value or an
array, the root of a small expression tree like:

.. figure:: doc/images/pow.png
   :alt: py ** 2

   py ^ 2

``x.log()`` evaluates to something as simple as

.. figure:: doc/images/log.png
   :alt: log(px)

   log(px)

And, finally, ``__add__`` gets called on this second tree, and can
generate the full expression

.. figure:: doc/images/full.png
   :alt: log(px) + py ** 2

   log(px) + py \*\* 2

..

   **Note:** Evaluation is *not* restricted to lambdas or simple
   functions. Function calls can be nested, modules can be provided for
   reuse… the code *is* evaluated, not parsed. There are some
   limitations: see the Caveats section.

Evaluation
----------

To actually remove any need for the interpreter, the nodes of the tree
are instances of C++ classes, exposed to the interpreter using
``boost::python``.

Every node on the tree inherits from the unimaginative-named class
``Node``, and each “type” of node overrides a method ``eval``, so it is
left to each concrete implementation how to evaluate itself.

To allow the tree to be evaluated thread-safely, once they are built
they can not be modified: values must be passed through the call stack.

Going back to our running example, once we have the tree, we can
evaluate it as

::

   "+"->eval(100, 5)
       "log"->eval(100, 5)
           "px"->eval(100, 5)
               px is the first placeholder => return 100
           log(100) => return 4.605
       "^"->eval(100, 5)
           "py"->eval(100, 5)
               py is the second placeholder => return 5
           "2"->eval(100, 5)
               Constant => return 2
           => return std::pow(5, 2)
       => return 4.605 + 25

Functions
---------

Unlike operators and methods, functions can be “injected” by the calling
code without requiring to dive into Pyston itself.

Two kind of functions are supported: with and without context.

Functions without context
~~~~~~~~~~~~~~~~~~~~~~~~~

Any good old callable that returns one of the supported types.

Functions with context
~~~~~~~~~~~~~~~~~~~~~~

When evaluating an expression, a dictionary of ``boost::any`` can be
passed along, so the caller can propagate to the registered function
anything it may need to perform.

This is useful, for instance, for functions that need to convert between
coordinate systems: this information is not available from the call, but
rather from where the function is called (namely, the context)

Object-like
-----------

Sometimes the variable passed to Python is an object with a set of
attributes, and not a simple data type. It could be, for instance, and
object with a given flux, radius, etc…

Pyston models this with a dictionary of basic values (double, int,
bool), which are, in turn, exposed to Python via the ``__getattr__``
method.

This method returns a ``Node`` that retrieves the value using the
attribute as key to another dictionary.

This approach works, but is has some limitations. We refer again to
Caveats.

Putting everything together
---------------------------

To make the usage easier, Pyston provides the class
``ExpressionTreeBuilder``, wrapping most the machinery in a more compact
API. Normally, this should be the entry point.

An ``ExpressionTreeBuilder`` is constructed with no parameters.

**Warning**: The Python interpreter is assumed to be initialized
beforehand.

It exposes just two method: ``registerFunction`` and ``build``

registerFunction
~~~~~~~~~~~~~~~~

Allows to register any additional, arbitrary function from the outside.
They can require context, or be context-free. The method will take care
of wrapping them either way. The functor *must* be copyable.

Registered functions are exposed in Python on the ``pyston`` namespace.

An example:

.. code:: c++

   void pixToWorldAlpha(const Context& ctx, double x, double y) {
     auto coord_system = boost::get<std::shared_ptr<CoordinateSystem>>(ctx.at("cs"));
     return coord_system.pix2world(x, y).alpha;
   }

   ...

   ExpressionTreeBuilder builder;
   builder.registerFunction("pixToWorldAlpha", &pixToWorldAlpha);

From Python

.. code:: python

   import pyston

   def get_world_parameters(x, y):
       ra = DependentParameter(lambda x,y: pyston.pixToWorldAlpha(x, y), x, y)                                        
       return ra, dec

build
~~~~~

Returns an ``ExpressionTree`` with the signature given as a template.
For instance:

.. code:: c++

   auto py_func = main_namespace["my_prior"];
   auto prior = builder.build<double(double)>(py_func);

The expression tree can be called with or without context, and exposes a
method ``isCompiled``, which can be used to check if the expression
could be built, or rather a fallback wrapper was returned (see
Fallback).

Fallback
--------

As already mentioned in Caveats, there are some limitations intrinsic to
the technique used here. The good news is that they can be caught early
on.

For instance, if a placeholder is used as a condition, an exception will
be thrown. If a method or operation is unknown, an exception will be
thrown.

If ``expressionTreeBuilder`` catches one of these, it will just keep a
reference to the original Python callable, wrap it making sure the GIL
is acquired when entering and released when leaving, and returns an
identically callable functor.

``isCompiled`` can be used to notify the user that this code path will
be slow, and the method ``reason`` to log why, in case the user wants to
terminate earlier (i.e maybe the function has been mistyped, and the
fallback will fail too).

.. _functions-1:

Functions
~~~~~~~~~

When functions are registered, actually two overloaded definitions are
set up in Python: one that receives ``Node``, so it can be used to build
a tree, and another one with the same signature (minus the context), so
it can also be called from Python and still evaluate correctly.

The fallback method will use a thread local for passing along the
context, so functions with context can still be used.

::

   exprTree(context, a, b)
       -> acquire GIL
       -> store context in a thread local
       -> call python callable with (a, b)
           -> [py] call to pyston.funcWithContext
               -> call funcWithContext(thread local context, a, b)
       -> release GIL

Objects
~~~~~~~

The dictionary of key/value is also exposed to Python with an
``__getattr__`` method, so they are interchangeable with their
placeholder.

Caveats
-------

Control flow
~~~~~~~~~~~~

The biggest caveat is that placeholders can **not** be used for flow
control, as they have no defined value, and flow operations can not be
overridden.

This is probable acceptable. Libraries as tensorflow give similar errors
if you try to use tensors on conditions:

``Using a tf.Tensor as a Python bool is not allowed.``

However, you can use control flow if the condition is *external* to the
function. For instance:

.. code:: python

   do_that = True

   def myfunc(x, y):
       if do_that:
           return np.abs(x) + y
       else:
           return y

That’s acceptable and will work **but** whatever value has the external
variable during the first call will determine the behavior. If it is
modified inside the function itself, the change will be ignored.

This is: externals can be used for configuration (number of iteration,
flags, constants, etc.)

Operators and methods
~~~~~~~~~~~~~~~~~~~~~

Pyston needs to know and implement operators and methods at compilation
time. If a numpy function not contemplated originally is missing, the
“compilation” will (sort of) fail. See the section Fallback for more
information on what happens next.

Data types
~~~~~~~~~~

Only ``double``, ``int64_t``, and ``bool`` POD types are supported.
``float``, ``int32_t`` and the rest need to be type casted.

Casting
~~~~~~~

On C++ nodes must know what type they hold. Pyston is capable to some
extent to do upcasting automatically: i.e. a multiplication between a
double and a bool will wrap the bool on a ``Cast`` node before creating
the multiplication one.

It works, but complicates things.

.. _objects-1:

Objects
~~~~~~~

The attribute type must be known beforehand for the just mentioned
reason. Therefore, when building the tree a “prototype” dictionary must
be provided: i.e. with ``0.`` for attributes that are float, or
``false`` for those that are boolean.

On the plus side, this allows to catch accesses to unknown attributes
soon.

This ain’t simple
-----------------

I said *the concept* was simple. The machinery to actually expose things
for multiple types, objects, functions with context, and all with
multiple signatures is not. This requires quite a bit of boilterplate.

Once the tree is built, it is fairly straightforward to understand and
evaluate.

Templating has been used extensively to reduce the code duplication, at
the expense of, well, C++ templates.

.. |Build Status| image:: https://travis-ci.com/astrorama/pyston.svg?branch=develop
   :target: https://travis-ci.com/astrorama/pyston
