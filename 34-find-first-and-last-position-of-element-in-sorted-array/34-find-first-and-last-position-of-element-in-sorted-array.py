class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = -1, -1
        n=len(nums)
        l,r = 0,n-1
        while l<=r:
            mid=(l+r)//2
            if (nums[mid]==target) and (mid==0 or nums[mid-1]<target):
                start=mid
                break
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        l,r = 0,n-1
        while l<=r:
            mid=(l+r)//2
            if (nums[mid]==target) and (mid==n-1 or nums[mid+1]>target):
                end=mid
                break
            elif nums[mid]>target:
                r=mid-1
            else:
                l=mid+1 
        return [start,end]