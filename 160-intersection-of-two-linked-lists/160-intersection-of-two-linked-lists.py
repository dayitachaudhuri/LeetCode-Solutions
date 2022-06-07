# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        n1,n2=0,0
        itrA,itrB=headA,headB
        while itrA:
            itrA=itrA.next
            n1+=1
        while itrB:
            itrB=itrB.next
            n2+=1
            
        itrA,itrB=headA,headB        
        if n2>n1:
            for i in range(n2-n1):
                itrB=itrB.next
        else:
            for i in range(n1-n2):
                itrA=itrA.next
        
        while itrA and itrB:
            if itrA==itrB:
                return itrA
            itrA=itrA.next
            itrB=itrB.next