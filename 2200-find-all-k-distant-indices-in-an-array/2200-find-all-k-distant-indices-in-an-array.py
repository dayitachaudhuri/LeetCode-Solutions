class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n=len(nums)
        nodes=[0]*n
        ans=[]
        for i in range(0,n):
            if nums[i]==key:
                for x in range(i-k,i+k+1):
                    if x>=0 and x<n:
                        nodes[x]+=1
        for i in range(n):
            if nodes[i]>0:
                ans.append(i)
        return ans