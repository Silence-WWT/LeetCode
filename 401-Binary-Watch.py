# -*- coding: utf-8 -*-
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        hours = {}
        minutes = {}
        times = []

        for i in range(60):
            count = bin(i).count('1')
            if i <= 11:
                if count not in hours:
                    hours[count] = []
                hours[count].append(i)
            if i <= 59:
                if count not in minutes:
                    minutes[count] = []
                minutes[count].append(i)

        for i in range(0, num + 1):
            j = num - i
            for h in hours.get(i, []):
                for m in minutes.get(j, []):
                    times.append('%d:%02d' % (h, m))

        return times
