class Solution:
    def climbStairs(self, n: int) -> int:
        cache={1:1,2:2}
        def dp(n):
            if n in cache:
                return cache[n]
            value=dp(n-1)+dp(n-2)
            cache[n]=value
            return value
        return dp(n)