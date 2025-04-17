# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # REDO 4/16/2025
    # AHA: WE RETURN THE END OF THE LL WHICH IS BEFORE, since it is the front now
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        before = after = None
        while temp:
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        return before
           

