class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cache=defaultdict(lambda:0)
        maxcount=0
        for i in nums:
            cache[i]+=1
        for i in range(0,len(nums)):
            if cache[nums[i]-1]==0:
                count=0
                curr=nums[i]
                while(cache[curr]>0):
                    count+=1
                    curr+=1
                if count>maxcount:
                    maxcount=count
        return maxcount