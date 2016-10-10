# -*- coding: utf-8 -*-
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        nums = {n}
        while True:
            n = sum(map(lambda x: int(x) * int(x), str(n)))
            if n == 1:
                return True
            elif n in nums:
                return False
            nums.add(n)
