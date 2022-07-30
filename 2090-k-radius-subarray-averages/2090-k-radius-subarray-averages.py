class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        
        currSum=0
        n=len(nums)
        ans=[-1]*n
        if n<2*k+1:
            return ans
        for i in range(0,2*k+1):
            currSum+=nums[i]
        currAv=currSum//(2*k+1)
        
        start=0
        end=2*k
        mid=k
        
        while end<n:
            ans[mid]=currAv
            if end<n-1:
                currSum=currSum+nums[end+1]-nums[start]
                currAv=currSum//(2*k+1)
            start+=1
            end+=1
            mid+=1
            
        return ans