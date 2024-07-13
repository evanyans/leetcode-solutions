# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find middle using Turtwa and the Hare
        front = head
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Reverse the second half (Reverse Linked List)
        temp = slow
        before = None
        after = None
        while temp:
            after = temp.next
            temp.next = before
            before = temp
            temp = after

        # Start the node alternating for reordering
        # we have front, and before to iterate through until 
        # their values are the same
        after = None
        after_alt = None
        while front != before and before.next:
            after = front.next
            front.next = before
            front = after

            after_alt = before.next
            before.next = front
            before = after_alt
            
        


        
        
            

            
     




