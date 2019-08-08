# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        curr = head
        prev = curr
        curr = curr.next
        while (curr != None):
            if prev.val == curr.val:
                if curr.next != None:
                    prev.next = curr.next
                else:
                    prev.next = None
                curr = curr.next
            else:
                prev = prev.next
                curr = curr.next
        return head


