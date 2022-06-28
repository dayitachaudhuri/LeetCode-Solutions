class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache={0:cost[0],1:cost[1]}
        nx=len(cost)
        for i in range(2,nx):
            cache[i]=cost[i]+min(cache[i-1],cache[i-2])
        
        return min(cache[nx-1],cache[nx-2])