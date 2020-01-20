# actually 101.py, verifying if tree is symmetric tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        q = deque([root])
        while(q):
            it = len(q)
            level = []
            for i in range(it):
                node = q.popleft()
                if node is None:
                    level.append(None)
                    continue
                level.append(node.val)
                for nn in [node.left, node.right]:
                    q.append(nn if nn is not None else None)
            if not level == level[::-1]:
                return False
        return True
    
    
        
