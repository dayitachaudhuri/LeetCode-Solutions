class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l,r=0,len(arr)-1
        while l<=r:
            mid=(l+r)//2
            if mid<len(arr)-1 and arr[mid]>arr[mid+1]:
                if mid>0 and arr[mid]>arr[mid-1]:
                    return mid
                else:
                    r=mid
            else:
                l=mid