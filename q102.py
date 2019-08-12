# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
    
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return
        queue = []
        ans = [[]]
        level = 0
        queue.append([root,level])
        print(queue)
        while (len(queue) > 0):
            node = queue.pop(0)
            # print('pop: ', node)
            if len(ans) <= level:
                ans.append([])
            ans[node[1]].append(node[0].val)
            level = node[1]
            # print('ans: ', ans)
            if node[0].left is not None or node[0].right is not None:
                level += 1
                if node[0].left is not None:
                    queue.append([node[0].left,level])
                if node[0].right is not None:
                    queue.append([node[0].right,level])
        return ans
        
            
        
