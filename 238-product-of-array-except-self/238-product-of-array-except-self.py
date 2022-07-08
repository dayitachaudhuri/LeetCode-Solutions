class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n=len(nums)
        answer=[1]*n
        prefix=[1]*n
        sufix=[1]*n
        
        for i in range(1,n):
            prefix[i]=prefix[i-1]*nums[i-1]
            sufix[n-i-1]=sufix[n-i]*nums[n-i]
        
        for i in range(0,n):
            answer[i]=prefix[i]*sufix[i]
        
        return answer