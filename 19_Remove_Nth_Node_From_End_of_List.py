"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 """
 # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        
        dummy = ListNode()
        dummy.next = head
        
        i = 0
        while head:
            i += 1
            head = head.next
        
        m = i - n
        
        first = dummy
        while m > 0:
            m -= 1
            first = first.next
        first.next = first.next.next    
        
        return dummy.next
        """
        left = right = head
        size = 1
        
        while right.next:
            size += 1
            right = right.next
            if size > n + 1:
                left = left.next
        if size == n:
            return head.next
        else:
            left.next = left.next.next
            return head
            