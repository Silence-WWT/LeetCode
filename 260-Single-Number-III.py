# -*- coding: utf-8 -*-
class Solution(object):
    def singleNumber(self, nums):
        """
        :param nums: List[int]
        :return: List[int]
        """
        a = b = diff = 0
        for num in nums:
            diff ^= num
        diff &= -diff
        for num in nums:
            if diff & num == 0:
                a ^= num
            else:
                b ^= num
        return [a, b]
