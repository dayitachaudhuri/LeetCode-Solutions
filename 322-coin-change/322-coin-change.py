class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache=[-1]*(amount+1)
        cache[0]=0
        def change(amount):
            if amount<0:
                return 99999
            if cache[amount]!=-1:
                return cache[amount]
            value=min(1+change(amount-i) for i in coins)
            cache[amount]=value
            return value
        
        res=change(amount)
        if res>=99999:
            return -1
        return res