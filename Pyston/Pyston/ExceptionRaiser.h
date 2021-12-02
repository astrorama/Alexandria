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

#ifndef PYSTON_EXCEPTIONRAISER_H
#define PYSTON_EXCEPTIONRAISER_H

#include "Pyston/Graph/Node.h"
#include "Pyston/PythonExceptions.h"
#include <boost/python/errors.hpp>
#include <memory>
#include <string>

namespace Pyston {

/**
 * Convenience functor that just raises a Python error whenever called.
 * It can be used to attach methods that can only fail to Python objects.
 * @tparam T
 *  Node type
 */
template <typename T>
class ExceptionRaiser {
public:
  /**
   * Constructor
   * @param msg
   *    Message for the exception
   * @param recoverable
   *    If true, the exception is considered to be recoverable (fallback python evaluation)
   */
  ExceptionRaiser(const std::string& msg, bool recoverable) : m_msg{msg}, m_recoverable{recoverable} {}

  /**
   * Callable
   * @throws boost::python::error_already_set
   *    Always. It will set previously a RuntimeError with the given message.
   */
  void operator()(const std::shared_ptr<Node<T>>&) {
    if (m_recoverable)
      throw RecoverableError(m_msg.c_str());
    else
      throw UnrecoverableError(m_msg.c_str());
  }

private:
  std::string m_msg;
  bool m_recoverable;
};

}  // end of namespace Pyston

#endif  // PYSTON_EXCEPTIONRAISER_H
