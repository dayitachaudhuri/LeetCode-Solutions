class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low=high=prices[0]
        prof=0
        if len(prices)==0:
            return prof
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                high=prices[i]
            else:
                if high!=low:
                    prof=prof+high-low
                high=low=prices[i]
        if low!=high:
            prof=prof+high-low
        return prof
                    