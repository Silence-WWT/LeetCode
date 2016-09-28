# -*- coding: utf-8 -*-
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if not num:
            return 0
        return num % 9 or 9
