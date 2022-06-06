# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        k=0
        itr=head
        while itr:
            k+=1
            itr=itr.next
        if k==n:
            return head.next
        itr=head
        prev=None
        for i in range(k-n):
            prev=itr
            itr=itr.next
        prev.next=itr.next
        itr.next=None
        return head