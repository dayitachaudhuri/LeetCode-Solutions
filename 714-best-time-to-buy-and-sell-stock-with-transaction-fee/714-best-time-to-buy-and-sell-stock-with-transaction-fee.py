class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cost=-prices[0]
        sell=0
        for i in range(1,len(prices)): 
            cost=max(cost,sell-prices[i])
            sell=max(sell,prices[i]+cost-fee)
        return sell