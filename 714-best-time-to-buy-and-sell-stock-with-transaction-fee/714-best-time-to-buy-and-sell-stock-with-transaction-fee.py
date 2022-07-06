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
                action = dfs(i+1,not hold) + prices[i] - fee
                
            # If not holding stock, we can buy it.
            else:
                action = dfs(i+1,not hold) - prices[i]
                
            # We can wait.
            wait = dfs(i+1, hold)
            
            # Update the hashmap with maximum of selling/buying and waiting.
            dp[(i,hold)] = max(action,wait)
            return dp[(i,hold)]
    
        return dfs(0,False)