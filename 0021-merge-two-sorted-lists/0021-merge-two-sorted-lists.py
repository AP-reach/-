# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #test empty nodes
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val > list2.val:
            list1 , list2 = list2 , list1

        ans = list1


        list3 = list1.next

        while list3 != None and list3.val < list2.val:
            list1 = list1.next
            list3 = list3.next

        if not list3:
            list1.next = list2
            return ans

        list1.next = list2
        n_list2 = list2.next
        list2.next = list3










        return self.mergeTwoLists(ans , n_list2)