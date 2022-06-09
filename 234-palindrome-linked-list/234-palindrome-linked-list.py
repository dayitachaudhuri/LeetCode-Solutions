# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:        
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
            s=[]
            itr=head
            while itr:
                s.append(itr.val)
                itr=itr.next
                
            for i in range(len(s)//2):
                if s[i]!=s[len(s)-i-1]:
                    return False
            return True