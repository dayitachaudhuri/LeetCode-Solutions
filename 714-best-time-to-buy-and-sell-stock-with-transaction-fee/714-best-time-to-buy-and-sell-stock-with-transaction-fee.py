class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        curr, res = prices[0] + fee, 0
        for i in prices[1:]:
            if i > curr:
                res += i - curr
                curr = i
            elif curr > i + fee:
                curr = i + fee
        return res