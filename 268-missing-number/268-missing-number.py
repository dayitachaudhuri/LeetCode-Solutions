class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        tot=0
        n=len(nums)
        for i in nums:
            tot+=i
        return (n*(n+1)//2)-tot