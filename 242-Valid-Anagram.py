# -*- coding: utf-8 -*-
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l = [0] * 26
        for c in s:
            l[ord(c) - ord('a')] += 1
        for c in t:
            l[ord(c) - ord('a')] -= 1
        for i in l:
            if not i:
                return False
        return True
