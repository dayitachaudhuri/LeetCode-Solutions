# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n=0
        itr=head
        while itr:
            itr=itr.next
            n+=1
        if n==0 or k%n==0:
            return head
        k=k%n
        prev=None
        itr=head
        for i in range(0,n-k):
            prev=itr
            itr=itr.next
        prev.next=None
        temp=itr
        while itr.next:
            itr=itr.next
        itr.next=head
        return temp
            
            