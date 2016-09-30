# -*- coding: utf-8 -*-
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        d = {}
        for c in magazine:
            d[c] = d.get(c, 0) + 1
        for c in ransomNote:
            v = d.get(c, 0)
            if not v:
                return False
            d[c] = v - 1
        return True
