
class Solution:
    def isHappy(self, n: int) -> bool:
        def sumofsq(num):
            res=0
            for i in list(str(num)):
                res+=int(i)**2
            return res
        
        cache=[]
        while n not in cache:
            cache.append(n)
            n=sumofsq(n)
            if n==1:
                return True
        return False