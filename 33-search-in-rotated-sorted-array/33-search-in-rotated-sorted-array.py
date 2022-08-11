class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n=len(nums)
        
        low,high=0,n-1
        
        while low<=high:
            
            mid=(low+high)//2
            
            if nums[mid]==target:
                return mid
            
            if nums[low]<=nums[mid]:
                if target>nums[mid] or target<nums[low]:
                    low=mid+1
                else:
                    high=mid-1
                    
            else:
                if target<nums[mid] or target>nums[high]:
                    high=mid-1
                else:
                    low=mid+1
                
        return -1