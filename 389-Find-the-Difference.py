# -*- coding: utf-8 -*-
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        a = 0
        for c in s:
            a ^= ord(c)
        for c in t:
            a ^= ord(c)
        return chr(a)
