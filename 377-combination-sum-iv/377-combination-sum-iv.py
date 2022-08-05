class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp={0:1}
        for total in range(1, target+1):
            dp[total]=0
            for val in nums:
                if val<=total:
                    dp[total]+=dp[total-val]
        return dp[target]