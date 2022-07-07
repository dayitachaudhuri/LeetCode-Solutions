class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans=[0]*len(nums)
        stack=[]
        for j in range(len(nums)-2,-1,-1):
            stack.append(nums[j])
        for i in range(len(nums)-1,-1,-1):
            while stack and stack[-1]<=nums[i]:
                stack.pop()
            if len(stack)==0:
                ans[i]=-1
            else:
                ans[i]=stack[-1]
            stack.append(nums[i])
        return ans