class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        cache={}
        count=0
        for i in nums:
            if i in cache:
                cache[i]+=1
            else:
                cache[i]=1
        for i in cache:
            if i+k in cache:
                count+=cache[i]*cache[i+k]
        return count