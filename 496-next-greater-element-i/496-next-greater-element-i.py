class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[nums2[-1]]
        ans={nums2[-1]:-1}
        for i in range(len(nums2)-2,-1,-1):
            while stack and stack[-1]<=nums2[i]:
                stack.pop()
            if len(stack)==0:
                ans[nums2[i]]=-1
            else:
                ans[nums2[i]]=stack[-1]
            stack.append(nums2[i])
            
        res=[]
        for val in nums1:
            res.append(ans[val])
        return res
            