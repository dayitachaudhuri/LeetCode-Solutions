# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        itr=head
        itrA=currA=ListNode()
        itrB=currB=ListNode()
        
        while itr:
            temp=itr.next
            if itr.val<x:
                itrA.next=itr
                itrA=itrA.next
            else:
                itrB.next=itr
                itrB=itrB.next
            itr.next=None
            itr=temp
        
        itrA.next=currB.next
        return currA.next