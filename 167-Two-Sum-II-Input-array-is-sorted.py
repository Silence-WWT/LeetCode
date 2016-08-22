# -*- coding: utf-8 -*-
class Solution(object):
    def twoSum(self, numbers, target):
        dic = {}
        for i, num in enumerate(numbers):
            if target - num in dic:
                return [dic[target - num] + 1, i + 1]
            dic[num] = i


class Solution2(object):
    """O(n)"""
    def twoSum(self, numbers, target):
        if len(numbers) == 2:
            return numbers
        left = 0
        right = len(numbers) - 1
        while left < right:
            value = numbers[left] + numbers[right]
            if value > target:
                right -= 1
            elif value < target:
                left += 1
            else:
                return [left + 1, right + 1]


class Solution3(object):
    """O(n*log n)"""

    @staticmethod
    def binary_search(numbers, target):
        left = 0
        right = len(numbers) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if numbers[mid] == target:
                return mid
            elif numbers[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1

    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index1 in range(0, len(numbers) // 2 + 1):
            index2 = self.binary_search(numbers, target - numbers[index1])
            if index2 > 0 and index2 != index1:
                break
        if index1 < index2:
            return [index1 + 1, index2 + 1]
        else:
            return [index2 + 1, index1 + 1]
