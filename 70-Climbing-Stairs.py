# -*- coding: utf-8 -*-
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2

        a, b = 1, 2
        for i in range(2, n):
            tmp = a + b
            a, b = b, tmp
        return b

    def climbStairs2(self, n):
        if n in (0, 1, 2):
            return n
        ways = [0] * n
        ways[0], ways[1] = 1, 2
        for i in range(2, n):
            ways[i] = ways[i - 1] + ways[i - 2]
        return ways[-1]
