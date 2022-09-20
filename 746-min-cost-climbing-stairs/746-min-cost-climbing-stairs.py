class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        dp={n:0,n+1:0}
        def sol(i):
            if i in dp:
                return dp[i]
            dp[i]=cost[i]+min(sol(i+1),sol(i+2))
            return dp[i]
        return min(sol(0),sol(1))
            