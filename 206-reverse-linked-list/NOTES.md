**RECURSIVE**
```
class Solution:
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
if not head or not head.next:
return head
node=self.reverseList(head.next)
head.next.next=head
head.next=None
return node
```
**ITERATIVE**
```
class Solution:
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
itr=head
prev=None
while itr:
temp=itr.next
itr.next=prev
prev=itr
itr=temp
return prev
```