# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def merge(self, headA, headB):
            curr=itr=ListNode()
            while headA and headB:
                if headA.val<=headB.val:
                    itr.next=ListNode(headA.val)
                    headA=headA.next
                else:
                    itr.next=ListNode(headB.val)
                    headB=headB.next
                itr=itr.next
            while headA:
                itr.next=ListNode(headA.val)
                headA=headA.next
                itr=itr.next
            while headB:
                itr.next=ListNode(headB.val)
                headB=headB.next
                itr=itr.next
            return curr.next
        
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if len(lists)==0:
            return None
        if len(lists)==1:
            return lists[0]
        
        temp=[]
        for i in range(0,len(lists)//2):
            temp.append(self.merge(lists.pop(), lists.pop()))
        if lists:
            temp.append(lists.pop())
        return self.mergeKLists(temp)
            
            