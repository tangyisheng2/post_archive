#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   FFT_FD.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2020, Tang Yisheng

@Modify Time        @Author     @Version        @Desciption
------------        -------     --------        -----------
2020/4/6 10:09     Tang        1.0             None
"""

import numpy
import math


def solve():
    original = list(range(0, 16))
    bit_len = math.ceil(math.log(len(original), 2))
    fd = numpy.zeros(len(original), dtype=int)
    for number in original:
        fd_index = 0
        for bit in range(0, bit_len):

            if number & 1 << bit:
                fd_index += 1 << (bit_len - bit - 1)

        fd[fd_index] = number

    print(fd)


if __name__ == "__main__":
    solve()
