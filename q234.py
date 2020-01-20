# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        num = []
        if head is None:
            return True
        while (head is not None):
            num.append(head.val)
            head = head.next
        return num == num[::-1]