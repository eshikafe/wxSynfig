# Synfig-Reloaded: mapping.pyx
# 
# Copyright (C) 2017 Austin Aigbe
# 
# This package is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of
# the License, or (at your option) any later version.
#
# This package is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
#  Based on mapping.hpp
#  brushlib - The MyPaint Brush Library. Copyright (C) 2007-2008 Martin Renold <martinxyz@gmx.ch>
#

from libc.stdlib cimport *
  
cdef struct ControlPoints:
  float xvalues[8]
  float yvalues[8]
  int n

# user-defined mappings
# (the curves you can edit in the brush settings)

cdef class Mapping:
  cdef ControlPoints *points_list
  cdef int inputs_used
  cdef float base_value

  def __init__(self, int input_):
    self.inputs = input_
    points_list = <ControlPoints*> malloc(sizeof(ControlPoints)*input_) # one for each input

    cdef int i = 0
    for i in range(input_):
      points_list[i].n = 0

    self.inputs_used = 0
    self.base_value = 0

  def __dealloc__(self):
    if (self.points_list != NULL):
      free(self.points_list)

  def set_n(self, int input_, int n):
    assert (input_ >= 0) and (input_ < self.inputs)
    assert (n >= 0) and (n <= 8)
    assert (n != 1)
    ControlPoints *p = self.points_list + input_

    if (n != 0) and (p.n == 0):
      self.points_list = self.inputs_used + 1
    if (n == 0) and (p.n != 0):
      self.inputs_used = self.inputs_used - 1

    assert(self.inputs_used >= 0)
    assert(self.inputs_used <= inputs)

    p.n = n

  def set_point(self, int input_, int index, float x, float y):
    assert (input_ >= 0) and (input_ < self.inputs)
    assert (index >= 0) and (index < 8)

    ControlPoints * p = self.points_list + input_
    assert (index < p.n)

    if (index > 0):
      assert x >= p.xvalues[index-1]

    p.xvalues[index] = x
    p.yvalues[index] = y

  def is_constant(self):
    return self.inputs_used == 0

  cdef calculate(self, float *data):
    cdef int i, j
    cdef float result
    cdef float x, y
    cdef float x0, y0, x1, y1

    result = self.base_value;

    # constant mapping (common case)
    if (self.inputs_used == 0):
      return result

    for j in range(self.inputs):
      ControlPoints *p = self.points_list + j
      if (p.n):    
        x = data[j]

        # find the segment with the slope that we need to use
        x0 = p.xvalues[0]
        y0 = p.yvalues[0]
        x1 = p.xvalues[1]
        y1 = p.yvalues[1]

        for i in range(2, p.n):
          if x > x1: 
            x0 = x1
            y0 = y1
            x1 = p.xvalues[i]
            y1 = p.yvalues[i]

        if (x0 == x1):
          y = y0
        else:
          # linear interpolation
          y = (y1*(x - x0) + y0*(x1 - x)) / (x1 - x0)

        result += y
    return result

  # used in python for the global pressure mapping
  def calculate_single_input(self, float input_):
    assert self.inputs == 1
    return self.calculate(&input_)
