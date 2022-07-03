
class Solution:
    def isHappy(self, n: int) -> bool:
        def sumofsq(num):
            res=0
            while num>0:
                res+=(num%10)**2
                num=num//10
            return res
        
        while n>=2:
            n=sumofsq(n)
            if n==1:
                return True
            if n==4:
                return False
        return True