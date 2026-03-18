# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        q = head
        qq = q.next
        initial = head
        count = 1
        while qq:
            q = q.next
            qq = qq.next
            count += 1

        cut = k % count

        if cut == 0:
            return head

        l = head
        t = 1
        
        while t < count - cut :
            l = l.next
            t += 1
        
        ans = l.next
        l.next = None
        q.next = initial

        return ans

        
        
            
            