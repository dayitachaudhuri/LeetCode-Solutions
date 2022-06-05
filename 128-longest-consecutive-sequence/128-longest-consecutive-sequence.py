class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return 1
        maxlen=1
        count=1
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]==1:
                count+=1
                if count>maxlen:
                    maxlen=count
            elif nums[i]!=nums[i-1]:
                count=1
        return maxlen