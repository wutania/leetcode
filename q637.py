# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if root is None:
            return []
        temp = self.sortByLevel(root, 0, [])
        result = []
        for i in range(len(temp)):
            total = 0.0
            count = 0
            for j in range(len(temp[i])):
                total += float(temp[i][j])
                count += 1
            result.append(total/float(count))
        return result
    
    def sortByLevel(self, root, level, temp):
        if root is None:
            return []
        level = level + 1
        if level > len(temp):
            temp.append([root.val])
        else:
            temp[level-1].append(root.val)
        self.sortByLevel(root.left, level, temp)
        self.sortByLevel(root.right, level, temp)
        
        return temp
