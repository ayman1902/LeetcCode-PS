# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        slow,fast=head,head
        while fast and fast.next:#MIDDLE
            slow,fast=slow.next,fast.next.next
        
        prev=None
        current=slow
        while current:#reverse
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node
        max_sum = 0
        first_half, second_half = head, prev
        while second_half:
            max_sum = max(max_sum, first_half.val + second_half.val)
            first_half = first_half.next
            second_half = second_half.next
        
        return max_sum