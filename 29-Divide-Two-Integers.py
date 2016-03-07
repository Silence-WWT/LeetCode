# -*- coding: utf-8 -*-
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = 1
        if not divisor or dividend == -2147483648 and divisor == -1:
            return 2147483647
        elif dividend < 0 and divisor < 0:
            dividend = abs(dividend)
            divisor = abs(divisor)
        elif dividend < 0 or divisor < 0:
            dividend = abs(dividend)
            divisor = abs(divisor)
            sign = 0
        quotient = 0
        while dividend >= divisor:
            temp = divisor
            multiple = 1
            while dividend >= temp << 1:
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            quotient += multiple
        return quotient if sign else -quotient
