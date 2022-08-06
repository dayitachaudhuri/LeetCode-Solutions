class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = -1, -1
        for i in range(0,len(nums)):
            if nums[i]==target:
                if start==-1 or i<start:
                    start=i
                if end==-1 or i>end:
                    end=i
        return [start,end]