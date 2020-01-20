# this exceeds time limit

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        
        a = headA
        b = headB
        ans = a

        while a.next is not None:
            # print("here")
            if b.next is not None and b.val != a.val:
                b = b.next
            elif b.next is None and b.val != a.val:
                b = headB
                a = a.next
                ans = a
            elif b.next is not None and a.val == b.val:
                a = a.next
                b = b.next
        if a.next is None:
            while b.next is not None:
                if b.val != a.val:
                    b = b.next 
        if a.val == b.val:
            return ans
        return None

# this works! 

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lenA = 0
        lenB = 0
        a = headA
        b = headB
        ans = None
        
        if headA is None or headB is None:
            return ans
        while (a is not None):
            lenA += 1
            a = a.next
        while (b is not None):
            lenB += 1
            b = b.next
        a = headA
        b = headB
        while (lenA > lenB):
            a = a.next
            lenA -= 1
        while (lenB > lenA):
            b = b.next
            lenB -= 1
        while (a is not None):
            if id(a) == id(b):
                return a
            a = a.next
            b = b.next
        return ans
                    
