# -*- coding: utf-8 -*-
from random import randint


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        value = self.head.val
        current = self.head.next
        i = 2
        while current:
            j = randint(0, i-1)
            if not j:
                value = current.val
            i += 1
            current = current.next
        return value
