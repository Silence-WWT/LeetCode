# -*- coding: utf-8 -*-
class Solution(object):
    depth = 0

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return 0 if not root else 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def traversal(self, node, depth):
        if node.left:
            self.traversal(node.left, depth + 1)
        if node.right:
            self.traversal(node.right, depth + 1)
        if not node.left and not node.right:
            self.depth = max(self.depth, depth)

    def maxDepth2(self, root):
        if not root:
            return 0
        self.traversal(root, 1)
        return self.depth
