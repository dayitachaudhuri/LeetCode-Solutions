# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        itrA=head
        itrB=head
        prev=None
        for i in range(n):
            itrB=itrB.next
        while itrB:
            prev=itrA
            itrA=itrA.next
            itrB=itrB.next
        if itrA==head:
            return head.next
        prev.next=itrA.next
        itrA.next=None
        return head