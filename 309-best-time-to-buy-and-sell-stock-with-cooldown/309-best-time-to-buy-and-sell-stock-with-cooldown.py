class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        dp = {}
        
        def dfs(i,hold):
            if i>=n:
                return 0
            if (i,hold) in dp:
                return dp[(i,hold)]
            if hold:
                action = dfs(i+2,not hold) + prices[i]
            else:
                action = dfs(i+1,not hold) - prices[i]
            wait = dfs(i+1, hold)
            dp[(i,hold)] = max(action,wait)
            return dp[(i,hold)]
    
        return dfs(0,False)