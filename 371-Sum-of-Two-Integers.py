# -*- coding: utf-8 -*-
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MAX = 0x7FFFFFFF
        MASK = 0xFFFFFFFF
        while b:
            carry = (a & b) & MASK
            a = (a ^ b) & MASK
            b = (carry << 1) & MASK
        return a if a <= MAX else a | ~MASK
