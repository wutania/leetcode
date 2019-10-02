# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if (head is None):
            return False
        node1 = head
        node2 = head
        
        while (node2.next is not None):
            node1 = node1.next
            if (node2.next.next is None):
                return False
            node2 = node2.next.next
            if (node1 == node2):
                break
        if (node2.next is None):
            return False
        node1 = head
        while (node1 != node2):
            node1 = node1.next
            node2 = node2.next
        return node1
