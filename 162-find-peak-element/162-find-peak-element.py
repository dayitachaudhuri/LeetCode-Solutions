class Solution:
    def findPeakElement(self, arr: List[int]) -> int:
 
        n=len(arr)
        if n==1:
            return 0
        if n==2:
            if arr[0]>arr[1]:
                return 0
            return 1
        l, r = 0, n-1
        
        # Binary Search 
        
        while l<=r:
            
            mid=(l+r)//2
            
            # If mid is Peak
            if (mid==0 or arr[mid]>arr[mid-1]) and (mid==n-1 or arr[mid]>arr[mid+1]):
                return mid
            
            # If mid is in slope up
            if mid==0 or (mid!=n-1 and arr[mid]<arr[mid+1]):
                l=mid+1
            
            # If mid is in slope down
            elif mid==n-1 or (mid!=0 and arr[mid]<arr[mid-1]):
                r=mid-1
                