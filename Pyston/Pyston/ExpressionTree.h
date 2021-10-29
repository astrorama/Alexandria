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

#ifndef PYSTON_EXPRESSIONTREE_H
#define PYSTON_EXPRESSIONTREE_H

#include "Pyston/Graph/Node.h"
#include <functional>

namespace Pyston {

/*
 * Declaration to allow for function-like templates
 */
template <typename Signature>
class ExpressionTree;

template <typename R>
class ExpressionTreeBase {
public:
  /**
   * @return
   *    True if the expression tree has been fully "compiled",
   *    false if there is a wrapped call to Python under the hood
   */
  bool isCompiled() const {
    return m_is_compiled;
  }

  /**
   * @return
   *    If isCompiled is false, return the reason for it
   */
  const Exception* reason() const {
    return m_reason.get();
  }

  /**
   * @return
   *    The root of the expression tree
   */
  const std::shared_ptr<Node<R>>& getTree() const {
    return m_root;
  }

protected:
  bool                       m_is_compiled;
  std::shared_ptr<Node<R>>   m_root;
  std::shared_ptr<Exception> m_reason;

  ExpressionTreeBase(bool compiled, const std::shared_ptr<Node<R>>& root, const std::shared_ptr<Exception>& reason_)
      : m_is_compiled(compiled), m_root(root), m_reason(reason_) {}
};

/**
 * Wraps a call to an expression tree. Specialized for parameters as a vector
 * of values
 * @tparam R
 *  Return type
 * @tparam T
 *  Argument type
 */
template <typename R, typename T>
class ExpressionTree<R(const std::vector<T>&)> : public ExpressionTreeBase<R> {
public:
  /**
   * Use the tree as a function
   * @param args
   *    Argument list
   */
  R operator()(const Context& context, const std::vector<T>& args) const {
    Arguments converted;
    std::copy(args.begin(), args.end(), std::back_inserter(converted));
    return m_root->eval(context, converted);
  }

  /**
   * Use the tree as a function
   * @param args
   *    Argument list
   */
  R operator()(const std::vector<T>& args) const {
    Arguments converted;
    std::copy(args.begin(), args.end(), std::back_inserter(converted));
    return m_root->eval({}, converted);
  }

private:
  using ExpressionTreeBase<R>::m_root;

  ExpressionTree(bool compiled, const std::shared_ptr<Node<R>>& root, const std::shared_ptr<Exception>& reason_)
      : ExpressionTreeBase<R>(compiled, root, reason_) {}

  friend class ExpressionTreeBuilder;
};

/**
 * Wraps a call to an expression tree. Specialized for the general case.
 * @tparam R
 *  Return type
 * @tparam Args
 *  Argument types
 */
template <typename R, typename... Args>
class ExpressionTree<R(Args...)> : public ExpressionTreeBase<R> {
public:
  /**
   * Use the tree as a function
   * @param args
   *    Argument list
   */
  R operator()(const Context& context, const Args&... args) const {
    return m_root->eval(context, args...);
  }

  /**
   * Use the tree as a function
   * @param args
   *    Argument list
   */
  R operator()(const Args&... args) const {
    return m_root->eval(Context{}, args...);
  }

private:
  using ExpressionTreeBase<R>::m_root;

  ExpressionTree(bool compiled, const std::shared_ptr<Node<R>>& root, const std::shared_ptr<Exception>& reason_)
      : ExpressionTreeBase<R>(compiled, root, reason_) {}

  friend class ExpressionTreeBuilder;
};

}  // end of namespace Pyston

#endif  // PYSTON_EXPRESSIONTREE_H
