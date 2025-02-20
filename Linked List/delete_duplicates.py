# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #Attempted 2/19/2025
    # aha: more node manipulation
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        
        while curr and curr.next:
            if curr.val == curr.next.val:
                tmp = curr.next.next
                curr.next = tmp
            else:
                curr = curr.next
                
        return head
