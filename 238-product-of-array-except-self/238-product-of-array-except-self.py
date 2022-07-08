class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n=len(nums)
        prefix=[1]*n
        
        # Find prefix product in one pass
        for i in range(1,n):
            prefix[i]=prefix[i-1]*nums[i-1]
        
        # Multiply sufix in second pass
        prod=1
        for i in range(n-1,-1,-1):
            prefix[i]=prefix[i]*prod
            prod=prod*nums[i]
        
        return prefix