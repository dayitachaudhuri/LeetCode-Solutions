class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        dp={0:0}
        def change(rem):
            if rem<0:
                return 99999999999
            if rem in dp:
                return dp[rem]
            dp[rem]=min(1+change(rem-i) for i in coins)
            return dp[rem]
        
        ans=change(amount)
        if ans>=99999999999:
            return -1
        return ans