# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        q = deque([root])
        count = 0
        while(q):
            it = len(q)
            count += 1
            for i in range(it):
                node = q.popleft()
                if node is None:
                    continue
                for nn in [node.left, node.right]:
                    q.append(nn if nn is not None else None)
        return count-1