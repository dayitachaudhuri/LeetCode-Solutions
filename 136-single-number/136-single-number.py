class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        xor=0
        
        for i in nums:
            xor=xor^i
            
        return xor