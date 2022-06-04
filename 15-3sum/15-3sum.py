class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        n=len(nums) 
        nums.sort()
        ans=[]
        for k in range(len(nums)):
            if k==0 or nums[k]!=nums[k-1]:
                i,j=k+1,n-1
                while i<j:
                    if nums[i]+nums[j]+nums[k]==0:
                        if [nums[k],nums[i],nums[j]] not in ans:
                            ans.append([nums[k],nums[i],nums[j]])
                        i+=1
                    elif nums[i]+nums[j]+nums[k]<0:
                        i+=1
                    else:
                        j-=1

        return ans