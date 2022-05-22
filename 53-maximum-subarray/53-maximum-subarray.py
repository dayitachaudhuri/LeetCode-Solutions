class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        temp=0
        maxSum=nums[0]
        for i in nums:
            temp+=i
            if temp>maxSum:
                maxSum=temp
            if temp<0:
                temp=0
        return maxSum