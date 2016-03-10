# -*- coding: utf-8 -*-
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        result = []
        while root or stack:
            while root:
                stack.append(root)
                result.append(root.val)
                root = root.left
            root = stack.pop(-1)
            root = root.right
        return result
