class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof=0
        buy=prices[0]
        sell=prices[0]
        for i in range(0,len(prices)-1):
            if prices[i]<prices[i+1]:
                sell=prices[i+1]
            else:
                prof+=sell-buy
                buy=sell=prices[i+1]
        prof+=sell-buy
        return prof