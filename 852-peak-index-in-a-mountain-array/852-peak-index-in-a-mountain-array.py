class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        n=len(arr)
        l, r = 0, n-1
        
        # Binary Search 
        
        while l<=r:
            
            if l==r:
                return l
            
            if l==r-1:
                if arr[l]>arr[r]:
                    return l
                else:
                    return r
            
            mid=(l+r)//2
            
            # If mid is peak
            if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
                return mid
            
            # If mid is in slope up
            if arr[mid]<arr[mid+1]:
                l=mid+1
            
            # If mid is in slope down
            else:
                r=mid-1
                
            