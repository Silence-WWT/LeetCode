# -*- coding: utf-8 -*-
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        l = []
        nums1.sort()
        nums2.sort()
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:  # nums1[i] == nums2[j]
                l.append(nums1[i])
                i += 1
                j += 1
        return l

    def intersect2(self, nums1, nums2):
        d = {}
        l = []
        for i in nums1:
            d[i] = d.get(i, 0) + 1
        for i in nums2:
            if d.get(i, 0):
                l.append(i)
                d[i] -= 1
        return l
