class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        cache={}
        
        for i in nums:
            if i in cache:
                cache[i]+=1
            else:
                cache[i]=1
                
        for val in cache:
            if cache[val]==1:
                return val