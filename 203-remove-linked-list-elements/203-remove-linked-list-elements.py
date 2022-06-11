# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        itr=head
        prev=None
        while itr:
            if itr.val==val:
                if prev:
                    prev.next=itr.next
                    itr.next=None
                    itr=prev.next
                else:
                    head=itr.next
                    itr.next=None
                    itr=head
            else:
                prev=itr
                itr=itr.next               

        return head