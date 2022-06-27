class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        
        cache=[0,1,2]+[-1]*(n+1)
        
        def stair(n):
            if cache[n]!=-1:
                return cache[n]
            value=stair(n-1)+stair(n-2)
            cache[n]=value
            return value
        
        return stair(n)