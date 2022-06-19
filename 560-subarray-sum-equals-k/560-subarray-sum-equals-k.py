class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = {0: 1}
        prefSum = 0
        count = 0
        for i in range(len(nums)):
            prefSum += nums[i]
            if prefSum-k in res:
                count += res[prefSum-k]
            if prefSum not in res:
                res[prefSum] = 0
            res[prefSum] += 1
        return count
                
            
                