# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        itra=list1
        itrb=list2
        prev=None
        while itra and itrb:
            if itra.val>itrb.val:
                if itra==list1:
                    list1=itrb
                else:
                    prev.next=itrb
                prev=itrb
                temp=itrb.next
                itrb.next=itra
                itrb=temp
            else:
                prev=itra
                itra=itra.next    

        if itrb:
            if prev:
                prev.next=itrb
            else:
                list1=itrb
            
        return list1