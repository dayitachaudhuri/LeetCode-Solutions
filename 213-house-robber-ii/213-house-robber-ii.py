class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0],nums[1])
        
        def helper(nums):
            if len(nums)==1:
                return nums[0]
            prev2=nums[0]
            prev1=max(nums[0],nums[1])
            for i in range(2,len(nums)):
                curr=max(prev1,nums[i]+prev2)
                prev2=prev1
                prev1=curr
            return prev1
        
        return max(helper(nums[1:]),helper(nums[:len(nums)-1]))