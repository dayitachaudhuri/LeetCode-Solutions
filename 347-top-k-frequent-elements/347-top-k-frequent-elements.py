class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cache=defaultdict(lambda:0)
        ans=[]
        for i in nums:
            cache[i]+=1
        cache=dict(sorted(cache.items(), key=lambda item: item[1], reverse=True))
        for i in range(0,k):
            ans.append(list(cache.keys())[i])
        return ans