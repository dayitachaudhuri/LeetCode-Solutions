class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n=len(nums)
        l,r=0,n-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                if mid==0 or nums[mid-1]<target:
                    return mid
                else:
                    r=mid-1
            else:
                if mid==n-1 or nums[mid+1]>target:
                    return mid+1
                else:
                    l=mid+1