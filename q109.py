# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursively get all the left sub trees and right sub trees
def _sortedListToBST(arr, start, end):
    if start > end:
        return
    mid = (start+end)/2

    root = TreeNode(arr[mid])
    
    root.left = _sortedListToBST(arr, start, mid-1)
    root.right = _sortedListToBST(arr, mid+1, end)
        
    return root

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head is None:
            return
        arr = []
        # while loop to change linkedlist into array
        while curr is not None:
            arr.append(curr.val)
            curr = curr.next
        # pass array into helper function (start = 0, end = len(arr)-1) -> index!
        return _sortedListToBST(arr, 0, len(arr)-1)

