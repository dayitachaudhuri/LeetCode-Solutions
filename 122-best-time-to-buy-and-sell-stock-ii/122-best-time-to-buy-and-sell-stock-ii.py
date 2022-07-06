class Solution:
    def maxProfit(self, prices: List[int]) -> int:
 
        n = len(prices)
        dp = {}
        
        def dfs(i,hold):
            
            # Base Cases
            if i>=n:
                return 0
            if (i,hold) in dp:
                return dp[(i,hold)]
            
            # If holding stock, we can sell it or wait.
            if hold:
                dp[(i,hold)] = max(dfs(i+1,not hold) + prices[i], dfs(i+1,hold))
                
            # If not holding stock, we can either buy it or wait.
            else:
                dp[(i,hold)] = max(dfs(i+1,not hold) - prices[i], dfs(i+1,hold))
                
            return dp[(i,hold)]
    
        return dfs(0,False)