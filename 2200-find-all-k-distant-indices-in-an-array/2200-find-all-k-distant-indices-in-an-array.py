class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n=len(nums)
        nodes=[]
        for i in range(0,n):
            if nums[i]==key:
                nodes+=[x for x in range(i-k,i+k+1) if x>=0 and x<n]
        return list(set(nodes))
                