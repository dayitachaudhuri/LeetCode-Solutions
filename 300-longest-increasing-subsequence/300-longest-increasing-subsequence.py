class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lst = [nums[0]] 
        for i in range(1, len(nums)):
            
            cur = nums[i]
            
            if lst[-1] < cur:
                
                lst.append(cur)
                continue
                
            left = 0
            right = len(lst)-1
            
            while left < right:
                
                mid = left + (right-left)//2
                
                if cur <= lst[mid]:
                    right = mid
                else:
                    left = mid+1
                    
            lst[right] = cur
                
        return len(lst) 