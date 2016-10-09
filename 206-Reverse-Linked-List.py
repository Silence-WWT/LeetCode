# -*- coding: utf-8 -*-
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        node = head
        while node:
            next = node.next
            node.next = prev
            prev = node
            node = next
        return prev

    def reverseList2(self, node, prev=None):
        if not node:
            return prev
        next = node.next
        node.next = prev
        return self.reverseList2(next, node)
