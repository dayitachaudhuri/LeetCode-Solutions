class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n=len(arr)
        l, r = 0, n-1
        while l<=r:
            mid=(l+r)//2
            if mid==0 or (mid!=n-1 and arr[mid]<arr[mid+1]):
                l=mid+1
            elif mid==n-1 or (mid!=0 and arr[mid]<arr[mid-1]):
                r=mid-1
            else:
                return mid