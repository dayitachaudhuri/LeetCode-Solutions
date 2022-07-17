class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        cache=[0]*n
        for val in nums:
            if val>0 and val<=n:
                cache[val-1]+=1
        for i in range(n):
            if cache[i]==0:
                return i+1
        return n+1