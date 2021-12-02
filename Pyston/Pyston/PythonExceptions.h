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
#ifndef PYSTON_PYTHONEXCEPTIONS_H
#define PYSTON_PYTHONEXCEPTIONS_H

#include <exception>

namespace Pyston {

/**
 * Thrown when building the expression tree causes an unrecoverable error:
 * i.e. access to an unknown object attribute, which will remain unknown
 * even if evaluated through Python
 */
class UnrecoverableError : public std::logic_error {
public:

  /**
   * Constructor
   * @param msg
   *    Error message
   */
  explicit UnrecoverableError(const std::string& msg) : std::logic_error(msg) {}

  virtual ~UnrecoverableError() = default;
};

/**
 * Thrown when building the expression tree causes a recoverable error:
 * i.e. using a placeholder on a conditional can be recovered (evaluated
 * using the Python interpreter) albeit slower
 */
class RecoverableError : public std::logic_error {
public:
  explicit RecoverableError(const std::string& msg) : std::logic_error(msg) {}
  virtual ~RecoverableError() = default;
};

}  // namespace Pyston

#endif  // PYSTON_PYTHONEXCEPTIONS_H
