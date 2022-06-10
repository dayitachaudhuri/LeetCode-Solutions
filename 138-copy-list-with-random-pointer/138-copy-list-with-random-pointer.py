"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        dummy=curr=Node(0)
        itr=head
        while itr:
            curr.next=Node(itr.val,None,itr.random)
            curr=curr.next
            itr.random=curr
            itr=itr.next
        curr=dummy.next
        while curr:
            if curr.random:
                curr.random=curr.random.random
            curr=curr.next
        return dummy.next