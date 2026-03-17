# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge2lists(list1 : Optional[ListNode], list2 : Optional[ListNode]) -> Optional[ListNode] :
            if not list1:
                return list2
            if not list2:
                return list1

            if list1.val <= list2.val:
                list1.next = merge2lists(list1.next,list2)
                return list1
            else:
                list2.next = merge2lists(list1,list2.next)
                return list2



        n = len(lists)
        if n == 0:
            return None
        if n == 1:
            return lists[0]
        if n == 2:
            return merge2lists(lists[0],lists[1])

        
        
        k = n//2
        return merge2lists( self.mergeKLists(lists[:k]) , self.mergeKLists(lists[k:]) )
        
