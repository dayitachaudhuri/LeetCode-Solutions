class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache=defaultdict(lambda:None)
        for i in range(0,len(nums)):
            if cache[nums[i]] is not None:
                return list([cache[nums[i]],i])
            diff=target-nums[i]
            cache[diff]=i
           