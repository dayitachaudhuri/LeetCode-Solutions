class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        nx=len(cost)
        if nx==1:
            return 0
        cache={0:cost[0],1:cost[1]}
        def stairs(n):
            if n in cache:
                return cache[n]
            minCost=cost[n]+min(stairs(n-1),stairs(n-2))
            cache[n]=minCost
            return minCost
        
        return min(stairs(nx-1),stairs(nx-2))