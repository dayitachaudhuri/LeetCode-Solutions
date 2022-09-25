# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        back=None
        itr=head
        for i in range(0,left-1):
            back=itr
            itr=itr.next
        c=0
        prev=itr
        itr=itr.next
        while c<right-left:
            temp=itr.next
            itr.next=prev
            prev=itr
            itr=temp
            c+=1
        if back:
            back.next.next=itr
            back.next=prev
        else:
            head.next=itr
            head=prev
        return head