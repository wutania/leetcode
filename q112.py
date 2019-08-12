# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# def _sum(root,sum):
#     if root is None:
#         return 
#     curr = root
#     sum = sum - curr.val
#     if sum == 0:
#         return 0
#     if sum < 0:
#         return -1
    
#     print("curr: ", curr)
#     print ("sum: ", sum)
#     if curr.left is not None:
#         _sum(curr.left, sum) 
#     if curr.right is not None:
#         _sum(curr.right, sum)
#     return sum

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        # if root is None:
        #     return
        # total = _sum(root, sum)
        # print("total: ", total)
        # if total == 0:
        #     return True
        # if total == -1:
        #     return False
        # else:
        #     return False
        
        if root is None:
            return
        if not root.left and not root.right:
            if root.val - sum == 0:
                return True
            if root.val - sum < 0:
                return False
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
        
        
#         if root is None:
#             return
#         queue = []
#         queue.append(root)
#         while len(queue)>0:
#             node = queue.pop(0)
#             sum = sum - node.val
#             print ("latest sum: ", sum)
            
#             if sum == 0:
#                 return True
#             if sum < 0:
#                 return False
            
#             if node.left is not None:
#                 queue.append(node.left)
#             if node.right is not None:
#                 queue.append(node.right)
            
#         if sum > 0:
#             return False
        
    
