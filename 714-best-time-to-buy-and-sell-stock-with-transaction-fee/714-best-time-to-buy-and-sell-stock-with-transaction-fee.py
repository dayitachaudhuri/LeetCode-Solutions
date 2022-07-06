class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        n = len(prices)
        dp = {}
        
        def dfs(i,hold):
            
            # Base Cases
            if i>=n:
                return 0
            if (i,hold) in dp:
                return dp[(i,hold)]
            
            # If holding stock, we can sell it and wait the coldown.
            if hold:
                dp[(i,hold)] = max(dfs(i+1,not hold) + prices[i] - fee, dfs(i+1,hold))
                
            # If not holding stock, we can buy it.
            else:
                dp[(i,hold)] = max(dfs(i+1,not hold) - prices[i], dfs(i+1,hold))
                
            return dp[(i,hold)]
    
        return dfs(0,False)