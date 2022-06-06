# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        itra=list1
        itrb=list2
        head=curr=ListNode()
        while itra and itrb:
            if itra.val<=itrb.val:
                temp=itra.next
                curr.next=itra
                itra.next=None
                itra=temp
            else:
                temp=itrb.next
                curr.next=itrb
                itrb.next=None
                itrb=temp
            curr=curr.next
        if itra:
            curr.next=itra
        if itrb:
            curr.next=itrb
        return head.next