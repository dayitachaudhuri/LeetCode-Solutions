class Solution:
    def climbStairs(self, n: int) -> int:
        cache=[-1]*max(3,(n+1))
        cache[0]=0
        cache[1]=1
        cache[2]=2
        
        def stair(n):
            if cache[n]!=-1:
                return cache[n]
            value=stair(n-1)+stair(n-2)
            cache[n]=value
            return value
        
        return stair(n)