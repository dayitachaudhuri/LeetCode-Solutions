class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low=high=prices[0]
        prof=0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                high=prices[i]
            else:
                prof+=high-low
                high=low=prices[i]
        if high!=low:
            prof+=high-low
        return prof