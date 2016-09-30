# -*- coding: utf-8 -*-
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        x = 0
        for c in s[::-1]:
            num += (ord(c) - ord('A') + 1) * (26 ** x)
            x += 1
        return num
