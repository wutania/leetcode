# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return
        
        # remove all cases where the first value is to be removed
        while(head and head.val == val):
            head = head.next
        
        # if the whole list is removed then return 
        if not head:
            return
        
        # else start removing the next ones 
        prev = head
        curr = prev.next
        
        while(curr is not None):
            if (curr.val == val):
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return head
        
        
        