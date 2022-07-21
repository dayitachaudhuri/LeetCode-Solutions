# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:      
    def reverseList(self, head: Optional[ListNode],n) -> Optional[ListNode]:
        newHead,oldHead = None,None
        curr = head
        for i in range(n):
            oldHead = curr.next
            curr.next = newHead
            newHead = curr
            curr = oldHead
        return newHead, head, curr
    
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        left, right = left-1,right-1
        l_end, r_head = None, None
        
        curr = head
        if left == 0: 
            rev_head, rev_tail, rev_next = self.reverseList(head, right-left+1)
            head = rev_head
        else:
            for i in range(left-1):
                curr = curr.next
            l_end = curr
            rev_head, rev_tail, rev_next = self.reverseList(l_end.next,right-left+1)
            l_end.next = rev_head
        if rev_next != None:
            rev_tail.next = rev_next
        return head