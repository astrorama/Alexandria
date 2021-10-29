/**
 * @copyright (C) 2012-2020 Euclid Science Ground Segment
 *
 * This library is free software; you can redistribute it and/or modify it under
 * the terms of the GNU Lesser General Public License as published by the Free
 * Software Foundation; either version 3.0 of the License, or (at your option)
 * any later version.
 *
 * This library is distributed in the hope that it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
 * FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
 * details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with this library; if not, write to the Free Software Foundation, Inc.,
 * 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
 */

#include "Pyston/ExpressionTreeBuilder.h"
#include "PythonFixture.h"
#include <boost/test/unit_test.hpp>
#include <boost/thread.hpp>

using namespace Pyston;
namespace py = boost::python;

static const int NTHREADS    = 8;
static const int NITERATIONS = 20;

/**
 * Wraps an std::function with three parameters, and call it
 * NITERATIONS times with random parameters, storing the results
 */
struct Worker {
  struct Evaluation {
    std::array<double, 3> params;
    double                result;

    Evaluation() {
      for (size_t i = 0; i < params.size(); ++i) {
        params[i] = drand48();
      }
      result = 0.;
    }
  };

  Worker(int id, std::function<double(double, double, double)> functor) : m_thread_id(id), m_functor(functor) {}

  Worker(const Worker&) = delete;

  void run(void) {
    for (int i = 0; i < NITERATIONS; ++i) {
      Evaluation evaluation;
      evaluation.result = m_functor(evaluation.params[0], evaluation.params[1], evaluation.params[2]);
      m_evaluations.emplace_back(evaluation);
    }
  }

  int                                           m_thread_id;
  std::function<double(double, double, double)> m_functor;
  std::vector<Evaluation>                       m_evaluations;
};

/**
 * Reference implementation of the functions that will be written in Python
 */
double equivalent(double x, double y, double z) {
  return (z > 0.5) ? std::sin(x) : std::log(y);
}

BOOST_AUTO_TEST_SUITE(Multithread_test)

/**
 * Use multiplication with a boolean to implement the conditional.
 * The expression can be "compiled" into a computing graph, which should be thread-safe
 */
BOOST_FIXTURE_TEST_CASE(MultithreadCompiled_test, PythonFixture) {
  ExpressionTreeBuilder builder;
  auto py_func = py::eval("lambda x, y, z: (z > 0.5) * np.sin(x) + (z <= 0.5) * np.log(y)", main_namespace);

  std::function<double(double, double, double)> func;
  {
    auto tree = builder.build<double(double, double, double)>(py_func);
    BOOST_CHECK(tree.isCompiled());
    BOOST_TEST_MESSAGE(textRepr(tree.getTree()));
    func = tree;
  }

  size_t lock_count_prev = GILLocker::getLockCount();

  std::vector<std::unique_ptr<Worker>> workers;
  boost::thread_group                  thread_group;
  for (int i = 0; i < NTHREADS; ++i) {
    workers.emplace_back(new Worker(i, func));
    thread_group.create_thread(std::bind(&Worker::run, workers.back().get()));
  }
  thread_group.join_all();

  for (const auto& worker : workers) {
    BOOST_CHECK_EQUAL(worker->m_evaluations.size(), NITERATIONS);
    for (auto& eval : worker->m_evaluations) {
      auto res_check = equivalent(eval.params[0], eval.params[1], eval.params[2]);
      BOOST_CHECK_CLOSE(res_check, eval.result, 1e-8);
    }
  }

  BOOST_CHECK_EQUAL(GILLocker::getLockCount() - lock_count_prev, 0);
}

/**
 * Use a conditional, which can not be "compiled" into a graph.
 * The Function object will transparently wrap the Python calls, including
 * the GIL lock/release to make them thread safe, and interchangeable with a compiled version
 */
BOOST_FIXTURE_TEST_CASE(MultithreadNotCompiled_test, PythonFixture) {
  ExpressionTreeBuilder builder;
  py::exec(R"PYCODE(
def with_conditional(x, y, z):
  if z > 0.5:
    return np.sin(x)
  else:
    return np.log(y)
)PYCODE",
           main_namespace);

  auto                                          py_func = main_namespace["with_conditional"];
  std::function<double(double, double, double)> func;
  {
    auto tree = builder.build<double(double, double, double)>(py_func);
    BOOST_CHECK(!tree.isCompiled());
    BOOST_TEST_MESSAGE(textRepr(tree.getTree()));
    func = tree;
  }

  size_t lock_count_prev = GILLocker::getLockCount();

  std::vector<std::unique_ptr<Worker>> workers;
  {
    GILReleaser         releaser(gil_state);
    boost::thread_group thread_group;
    for (int i = 0; i < NTHREADS; ++i) {
      workers.emplace_back(new Worker(i, func));
      thread_group.create_thread(std::bind(&Worker::run, workers.back().get()));
    }
    thread_group.join_all();
  }

  for (const auto& worker : workers) {
    BOOST_CHECK_EQUAL(worker->m_evaluations.size(), NITERATIONS);
    for (auto& eval : worker->m_evaluations) {
      auto res_check = equivalent(eval.params[0], eval.params[1], eval.params[2]);
      BOOST_CHECK_CLOSE(res_check, eval.result, 1e-8);
    }
  }

  BOOST_CHECK_GT(GILLocker::getLockCount() - lock_count_prev, 0);
}

BOOST_AUTO_TEST_SUITE_END()
