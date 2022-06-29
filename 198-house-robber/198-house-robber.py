class Solution:
    def rob(self, nums: List[int]) -> int:
        dp=[-1]*(len(nums)+1)
        def helper(n):
            if n<0:
                return 0
            if dp[n]!=-1:
                return dp[n]
            dp[n]=max(helper(n-1),nums[n]+helper(n-2))
            return dp[n]
        return helper(len(nums)-1)