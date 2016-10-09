# -*- coding: utf-8 -*-
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and 1073741824 % n == 0  # n > 0 and n&(n-1) == 0
