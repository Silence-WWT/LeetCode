# -*- coding: utf-8 -*-
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        nums = {'I': 1, 'X': 10, 'C': 100, 'M': 1000, 'V': 5, 'L': 50, 'D': 500}
        s = s[::-1]
        flag = 1
        sum = 0
        for index in range(0, len(s)):
            if index > 0 and nums[s[index]] > nums[s[index - 1]]:
                flag = 1
            elif index > 0 and nums[s[index]] < nums[s[index - 1]]:
                flag = -1
            sum += flag * nums[s[index]]
        return sum
