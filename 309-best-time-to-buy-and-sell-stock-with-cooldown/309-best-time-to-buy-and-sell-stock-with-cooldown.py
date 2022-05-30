class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = [[0,0] for i in range(len(prices)+2)]
        for i in range(len(prices)-1,-1,-1):
            maxProfit[i][0] = max(maxProfit[i+1][1]-prices[i], maxProfit[i+1][0])
            maxProfit[i][1] = max(maxProfit[i+2][0]+prices[i], maxProfit[i+1][1])
        return maxProfit[0][0]