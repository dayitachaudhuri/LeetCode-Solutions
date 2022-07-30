class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        cache={}
        for i in nums:
            if i in cache:
                return True
            cache[i]=1
        return False