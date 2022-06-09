# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:        
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        def reverse(head):
            itr=head
            prev=None
            while itr:
                temp=itr.next
                itr.next=prev
                prev=itr
                itr=temp
            return prev
        
        slow,fast=head,head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        
        slow.next=reverse(slow.next)
        slow=slow.next
        itr=head
        while slow:
            if itr.val!=slow.val:
                return False
            itr=itr.next
            slow=slow.next
        return True
            
                    