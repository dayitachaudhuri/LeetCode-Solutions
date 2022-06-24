class Solution:
    def fib(self, n: int) -> int:
        dp={0:0,1:1,2:1}
        def helper(n):
            if n in dp:
                return dp[n]
            return helper(n-1)+helper(n-2)
        return helper(n)