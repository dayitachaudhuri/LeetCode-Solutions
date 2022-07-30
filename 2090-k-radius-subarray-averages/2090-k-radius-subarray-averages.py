class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        
        prefix={0:0}
        n=len(nums)
        ans=[-1]*n
        for i in range(1,n):
            prefix[i]=prefix[i-1]+nums[i-1]
        
        start=0
        end=2*k
        mid=k
        
        while end<n:
            ans[mid]=(prefix[end]-prefix[start]+nums[end])//(2*k+1)
            start+=1
            end+=1
            mid+=1
            
        return ans