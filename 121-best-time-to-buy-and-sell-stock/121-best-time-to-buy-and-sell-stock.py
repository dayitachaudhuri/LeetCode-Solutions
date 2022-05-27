class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minVal,prof=prices[0],0
        for i in range(0,len(prices)):
            if prices[i]<minVal:
                minVal=prices[i]
            elif prices[i]-minVal>prof:
                prof=prices[i]-minVal
        return prof