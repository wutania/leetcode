# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def untangle(x,y):
    if x is not None:
        _inOrder(x,y)
    print("this is the list: ", y)
    return y
def _inOrder(x,y):
    if x is None:
        return y
    _inOrder(x.left,y)
    if x.val is None:
        y.append(-1)
    else:
        y.append(x.val)
    _inOrder(x.right,y)
        
class Solution(object):
    
        
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        y = []
        z = []
        
        if p is not q:
            if (untangle(p,y) == untangle(q,z)):
                return True
            else:
                return False
        else:
            return True
        
        #this doesn't takes into account the case where [1,2] vs [1,null,2] is different :(
