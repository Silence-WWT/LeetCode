# -*- coding: utf-8 -*-
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        nums = {n}
        while True:
            n = sum(int(i) ** 2 for i in str(n))
            if n == 1:
                return True
            elif n in nums:
                return False
            nums.add(n)

    def isHappy2(self, n):
        def get_sum(n):
            return sum(int(i) ** 2 for i in str(n))

        slow = get_sum(n)
        fast = get_sum(get_sum(n))
        while slow != fast:
            slow = get_sum(slow)
            fast = get_sum(get_sum(fast))
        if slow == 1:
            return True
        return False
