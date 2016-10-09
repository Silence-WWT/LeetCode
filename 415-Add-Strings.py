# -*- coding: utf-8 -*-
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = num1[::-1]
        num2 = num2[::-1]
        length1 = len(num1)
        length2 = len(num2)
        num3 = []
        carry = 0

        for index in range(max(length1, length2)):
            a = b = 0
            if index < length1:
                a = int(num1[index])
            if index < length2:
                b = int(num2[index])
            c = a + b + carry
            carry = c // 10
            num3.append(str(c % 10))

        if carry:
            num3.append('1')
        return ''.join(num3)[::-1]
