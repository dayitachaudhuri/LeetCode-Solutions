# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes=[]
        for head in lists:
            while head:
                nodes.append(head.val)
                head=head.next
        nodes.sort()
        curr=itr=ListNode()
        for v in nodes:
            itr.next=ListNode(v)
            itr=itr.next
        return curr.next