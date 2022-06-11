class Solution:
    def listtoStack(self, head: Optional[ListNode]) -> list:
        itr=head
        arr=[]
        while itr:
            arr.append(itr.val)
            itr=itr.next
        return arr
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        arr1=self.listtoStack(l1)
        arr2=self.listtoStack(l2)
        head=ListNode()
        carry=0
        while(len(arr1)!=0 or len(arr2)!=0 or carry!=0):
            if (arr1):
                carry+=arr1.pop()
            if (arr2):
                carry+=arr2.pop()
            head.val=carry%10
            newNode=ListNode()
            newNode.next=head
            head=newNode
            carry=carry//10
            
        return head.next