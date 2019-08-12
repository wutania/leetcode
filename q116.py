"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        level = 0
        if root is None:
            return
        queue = []
        ans = [[]]
        queue.append([root, level])
        while len(queue)>0:
            node = queue.pop(0)
            if len(ans) <= level:
                ans.append([])
            ans[node[1]].append(node[0])
            level = node[1]
            if node[0].left is not None or node[0].right is not None:
                if node[0].left is not None:
                    queue.append([node[0].left, level])
                if node[0].right is not None:
                    queue.append([node[0].right, level])
        # ans now contains the nodes in leveled order 
        print ("ans: ", ans)
        for i in range(len(ans)):
            for j in range(len(ans[i])):
                if i == 0 and j == 0:
                    ans[i][j].next = None
                if j == len(ans[i])-1:
                    ans[i][j].next = None
                if j >= 1:
                    ans[i][j-1].next = ans[i][j]
        return root

# there is an bug here, need to fix later.

