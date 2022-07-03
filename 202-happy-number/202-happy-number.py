
class Solution:
    def isHappy(self, n: int) -> bool:
        def sumofsq(num):
            res=0
            while num>0:
                res+=(num%10)**2
                num=num//10
            return res
        
        slow,fast=n,n
        while True:
            slow=sumofsq(slow)
            fast=sumofsq(sumofsq(fast))
            if slow==1 or fast==1:
                return True
            if slow==fast:
                return False