class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp={}
        def solution(i):
            if i>=n:
                return 0
            if i in dp:
                return dp[i]
            dp[i]=max(nums[i]+solution(i+2),solution(i+1))
            return dp[i]
        
        return solution(0)