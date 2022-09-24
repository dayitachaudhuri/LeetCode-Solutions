class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        dp=[9999999999]*(amount+1)
        dp[0]=0
        for i in range(amount+1):
            for val in coins:
                if val<=i:
                    dp[i]=min(dp[i],1+dp[i-val])
        if dp[amount]==9999999999:
            return -1
        return dp[amount]