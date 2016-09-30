# -*- coding: utf-8 -*-
class Solution(object):

    sum = 0

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sum_values(root, is_left=False)
        return self.sum

    def sum_values(self, node, is_left):
        if not node:
            return
        if not node.left and not node.right and is_left:
            self.sum += node.val
            return
        self.sum_values(node.left, is_left=True)
        self.sum_values(node.right, is_left=False)
