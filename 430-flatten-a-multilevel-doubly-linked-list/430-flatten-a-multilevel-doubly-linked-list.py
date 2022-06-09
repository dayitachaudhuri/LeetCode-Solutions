"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        itr=head
        while itr:
            if itr.child:
                curr=itr.child
                while curr.next:
                    curr=curr.next
                if itr.next:
                    curr.next=itr.next
                    curr.next.prev=curr
                itr.next=itr.child
                itr.next.prev=itr
                itr.child=None
            itr=itr.next
        return head
                        
            
            
            