class Solution:
    def climbStairs(self, n: int) -> int:
        cache={0:0,1:1,2:2}
        
        def stair(n):
            if n in cache:
                return cache[n]
            value=stair(n-1)+stair(n-2)
            cache[n]=value
            return value
        
        return stair(n)