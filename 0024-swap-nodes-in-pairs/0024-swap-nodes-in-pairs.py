# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = head
        if not l:
            return head
        r = head.next
        if not r:
            return head
        
        nh = r.next
        r.next = l
        l.next = self.swapPairs(nh)
        return r
