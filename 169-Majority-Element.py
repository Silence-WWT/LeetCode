# -*- coding: utf-8 -*-
class Solution(object):
    def majorityElement2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for n in nums:
            d[n] = d.get(n, 0) + 1
        majority = len(nums) // 2
        for i in d:
            if d[i] > majority:
                return i

    def majorityElement(self, nums):
        major = nums[0]
        count = 1
        for i in nums[1:]:
            if count == 0:
                major = i
                count += 1
            elif major == i:
                count += 1
            else:
                count -= 1
        return major
