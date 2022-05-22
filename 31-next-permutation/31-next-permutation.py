class Solution:

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(arr: List[int]) -> List[int]:
            return arr[::-1]
        
        n=len(nums)
        if n<=1:
            return
        i=n-1
        while nums[i]<=nums[i-1]:
            i-=1
            if i==0:
                i-=1
                break
        if i==-1:
            nums[:]=reverse(nums[:])
        else:
            j=i
            while j<n and nums[j]>nums[i-1]:
                j+=1
            nums[i-1],nums[j-1]=nums[j-1],nums[i-1]
            nums[i:]=reverse(nums[i:])