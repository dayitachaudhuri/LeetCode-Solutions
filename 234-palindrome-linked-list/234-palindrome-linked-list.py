# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:        
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
            n=0
            itr=head
            while itr:
                itr=itr.next
                n+=1
            count=n//2
            stack=[]
            itr=head
            for i in range(count):
                stack.append(itr.val)
                itr=itr.next
            if n>1 and n%2!=0:
                itr=itr.next
            while itr:
                if len(stack)!=0 and itr.val!=stack.pop():
                    return False
                itr=itr.next
            return True