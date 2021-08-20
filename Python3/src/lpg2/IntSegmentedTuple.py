#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# This Tuple class can be used to construct a dynamic
# array of integers. The space for the array is allocated in
# blocks of size 2**LOG_BLKSIZE. In declaring a tuple the user
# may specify an estimate of how many elements he expects.
# Based on that estimate, suitable values will be calculated
# for log_blksize and base_increment. If these estimates are
# found to be off later, more space will be allocated.
#
from Utils import arraycopy


class IntSegmentedTuple(object):

    def __init__(self, log_blksize_: int = None, base_size_: int = None):
        self.top: int = 0
        self._size: int = 0

        self.log_blksize: int = 3
        self.base_size: int = 4

        self.base = []
        if log_blksize_ is not None:
            self.log_blksize = log_blksize_
        if base_size_ is not None:
            self.base_size = 4 if base_size_ <= 0 else base_size_

        self.base = [[]] * self.base_size

    #
    # Allocate another block of storage for the dynamic array.
    #
    def allocateMoreSpace(self):
        #
        # The variable size always indicates the maximum int of
        # elements that has been allocated for the array.
        # Initially, it is set to 0 to indicate that the array is empty.
        # The pool of available elements is divided into segments of size
        # 2**log_blksize each. Each segment is pointed to by a slot in
        # the array base.
        #
        # By dividing size by the size of the segment we obtain the
        # index for the next segment in base. If base is full, it is
        # reallocated.
        #
        #
        k: int = self._size >> self.log_blksize  # which segment?

        #
        # If the base is overflowed, reallocate it and initialize the 
        # elements to NULL.
        # Otherwise, allocate a  segment and place its adjusted address
        # in base[k]. The adjustment allows us to index the segment directly,
        # instead of having to perform a subtraction for each reference.
        # See operator[] below.
        #
        #
        if k == self.base_size:
            self.base_size *= 2
            self.base = arraycopy(self.base, 0, [[]] * self.base_size, 0, k)

        self.base[k] = [0] * (1 << self.log_blksize)

        #
        # Finally, we update SIZE.
        #
        self._size += (1 << self.log_blksize)

        return

    #
    # This function is invoked with an integer argument n. It ensures
    # that enough space is allocated for n elements in the dynamic array.
    # I.e., that the array will be indexable in the range  (0..n-1):
    #
    # Note that self function can be used as a garbage collector.  When
    # invoked with no argument(or 0):, it frees up all dynamic space that
    # was allocated for the array.
    #
    def resize(self, n: int = 0):
        #
        # If array did not previously contain enough space, allocate
        # the necessary additional space. Otherwise, if the array had
        # more blocks than are needed, release the extra blocks.
        #
        if n > self._size:
            while True:
                self.allocateMoreSpace()
                if not n > self._size:
                    break
        self.top = n

    #
    # This function is used to reset the size of a dynamic array without
    # allocating or deallocting space. It may be invoked with an integer
    # argument n which indicates the  size or with no argument which
    # indicates that the size should be reset to 0.
    #
    def reset(self, n: int = 0):
        self.top = n
    #
    # Return size of the dynamic array.
    #

    def size(self) -> int:
        return self.top

    #
    # Can the tuple be indexed with i?
    #
    def outOfRange(self, i: int):
        return i < 0 or i >= self.top

    #
    # Return a reference to the ith element of the dynamic array.
    #
    # Note that no check is made here to ensure that 0 <= i < top.
    # Such a check might be useful for debugging and a range exception
    # should be thrown if it yields True.
    #
    def get(self, i: int) -> int:

        return self.base[i >> self.log_blksize][i % (1 << self.log_blksize)]

    #
    # Insert an element in the dynamic array at the location indicated.
    #
    def set(self, i: int, element: int):

        self.base[i >> self.log_blksize][i % (1 << self.log_blksize)] = element

    #
    # Add an element to the dynamic array and return the top index.
    #
    def NextIndex(self) -> int:
        i: int = self.top
        self.top += 1
        if i == self._size:
            self.allocateMoreSpace()

        return i

    #
    # Add an element to the dynamic array and return a reference to
    # that  element.
    #
    def add(self, element: int):
        i: int = self.NextIndex()
        self.base[i >> self.log_blksize][i % (1 << self.log_blksize)] = element

    #
    # If array is sorted, self function will find the index location
    # of a given element if it is contained in the array. Otherwise, it
    # will return the negation of the index of the element prior to
    # which the  element would be inserted in the array.
    #
    def binarySearch(self, element: int) -> int:

        low: int = 0
        high: int = self.top
        while high > low:
            mid: int = (high + low) // 2
            mid_element: int = self.get(mid)
            if element == mid_element:
                return mid
            else:
                if element < mid_element:
                    high = mid
                else:
                    low = mid + 1
        return -low

