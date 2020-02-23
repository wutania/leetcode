# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        curr = root
        if curr:
            temp = curr.left
            curr.left = curr.right
            curr.right = temp
            curr.left = self.invertTree(curr.left)      # invert the left side
            curr.right = self.invertTree(curr.right)    # invert the right side!
        return root
