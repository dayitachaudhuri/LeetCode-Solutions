class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        dp={}
        def coin(i,rem):
            if rem==0:
                return 0
            if rem<0 or i>=n:
                return 99999
            if (i,rem) in dp:
                return dp[(i,rem)]
            dp[(i,rem)]=min(1+coin(i,rem-coins[i]),coin(i+1,rem))
            return dp[(i,rem)]
        
        ans=coin(0,amount)
        if ans==99999:
            return -1
        return ans