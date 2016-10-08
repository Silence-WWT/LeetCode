# -*- coding: utf-8 -*-
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        count = 0
        for c in s:
            d[c] = d.get(c, 0) + 1
            if d[c] == 2:
                d[c] = 0
                count += 2
        for v in d.itervalues():
            if v == 1:
                count += 1
                break
        return count
