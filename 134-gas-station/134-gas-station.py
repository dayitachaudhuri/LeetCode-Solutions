class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n=len(gas)
        sum_gas=sum(gas)
        sum_cost=sum(cost)
        if sum_gas<sum_cost:
            return -1
        curr_gas=0
        curr_start=0
        for i in range(n):
            curr_gas+=gas[i]-cost[i]
            if curr_gas<0:
                curr_gas=0
                curr_start=i+1
        return curr_start