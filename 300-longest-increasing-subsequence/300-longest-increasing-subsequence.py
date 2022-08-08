class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []
        for num in nums:
            if len(res) == 0 or num > res[-1]:
                res.append(num)
            else:
                index = bisect.bisect_left(res, num)
                res[index] = num

        return len(res)