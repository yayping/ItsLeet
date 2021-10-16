"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 
 """
class Solution(object):
  def deleteDuplicates(self, head):
      """
      :type head: ListNode
      :rtype: ListNode
      """
      if not head:
          return head
      dummy = op = ListNode(0)
      while head.next:
          if head.val != head.next.val:
              op.next = head
              op = op.next
          head = head.next
      op.next = head
      return dummy.next