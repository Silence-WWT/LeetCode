# -*- coding: utf-8 -*-
class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        MAX = 2 ** 32
        chars = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
                 10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}

        if not num:
            return '0'

        if num < 0:
            num += MAX
        s = []
        while num:
            s.append(chars[num & 0xf])
            num >>= 4
        return ''.join(s)[::-1]
