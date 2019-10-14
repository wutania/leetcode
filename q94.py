# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        return self.traverse(root, ans)
        
    def traverse(self, root, ans):
        if root is None:
            return ans
        self.traverse(root.left, ans)
        ans.append(root.val)
        self.traverse(root.right, ans)
        return ans


