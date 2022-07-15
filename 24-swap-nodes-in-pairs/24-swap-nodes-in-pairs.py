# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        itr=head
        head=head.next
        prev=None
        while itr and itr.next:
            temp=itr.next.next
            itr.next.next=itr
            if prev:
                prev.next=itr.next
            prev=itr
            itr.next=temp
            itr=itr.next
        return head