/*
 * Copyright (C) 2012-2020 Euclid Science Ground Segment    
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

/* 
 * @file memory_tools.h
 * @author nikoapos
 */

#ifndef _ALEXANDRIAKERNEL_MEMORY_TOOLS_H
#define _ALEXANDRIAKERNEL_MEMORY_TOOLS_H

namespace Euclid {

/**
 * @brief
 * Constructs an object of type T and wraps it in a std::unique_ptr using args
 * as the parameter list for the constructor of T
 * @param args
 *    list of arguments with which the instance of T will be constructed
 * @return
 *    std::unique_ptr of the instance of type T
 */
template<typename T, typename... Args>
std::unique_ptr<T> make_unique(Args&&... args)
{
    return std::unique_ptr<T>(new T(std::forward<Args>(args)...));
}

}

#endif /* _ALEXANDRIAKERNEL_MEMORY_TOOLS_H */

