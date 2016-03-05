# -*- coding: utf-8 -*-


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def oddEvenList(self, head):
        """
        :param head: ListNode
        :return: ListNode
        """
        odd_head = odd = ListNode(None)
        even_head = even = ListNode(None)
        while head is not None:
            odd.next = head
            even.next = head.next
            odd = odd.next
            even = even.next
            head = head.next.next if even else None
        odd.next = even_head.next
        return odd_head.next
