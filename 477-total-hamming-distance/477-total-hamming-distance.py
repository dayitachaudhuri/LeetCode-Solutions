class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        ans = 0
        l = len(nums)
        tmp = 1
        
        for n in range(30):
            count = 0
            for k in range(l):
                if (nums[k] & tmp):
                    count += 1
        
            ans += count * (l-count)
            tmp <<= 1
        
        return ans