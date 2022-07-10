class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def xor(i,curr):
            if i>len(nums)-1:
                return curr
            return xor(i+1,curr^nums[i])+xor(i+1,curr)
        return xor(0,0)