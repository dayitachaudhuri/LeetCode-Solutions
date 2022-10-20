class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        pos=[0]*n
        for i in nums:
            if i>0 and i<=n:
                pos[i-1]=1
        for i in range(0,n):
            if pos[i]==0:
                return i+1
        return n+1