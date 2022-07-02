# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        slow,prev=head,head
        fast=head.next
        change=False
        
        while fast:
            if fast.val==slow.val:
                change=True    
            else:
                if change:
                    if slow==head:
                        head=fast
                        slow,prev=head,head
                    else:
                        prev.next=fast
                        slow=prev.next
                    change=False
                else:
                    prev=slow
                    slow=fast
            fast=fast.next
            
        if change==True:
            if prev==head and slow==head:
                head=None
            else:
                prev.next=None
        return head