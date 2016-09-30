# -*- coding: utf-8 -*-
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pos = 0
        for num in nums:
            if num:
                nums[pos] = num
                pos += 1
        while pos < len(nums):
            nums[pos] = 0
            pos += 1
        return nums
