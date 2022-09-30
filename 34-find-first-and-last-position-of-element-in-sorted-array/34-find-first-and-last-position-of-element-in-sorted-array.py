class Solution:
    def searchRange(self, arr: List[int], target: int) -> List[int]:
        start, end = -1, -1
        n=len(arr)
        
        # Binary Search to find First Position
        l,r = 0,n-1
        while l<=r:
            if l==r:
                if arr[l]==target:
                    start=l
                break
            if l==r-1:
                if arr[l]==target:
                    start=l
                elif arr[r]==target:
                    start=r
                break
            mid=(l+r)//2
            if arr[mid]==target and arr[mid-1]<target:
                start=mid
                break
            elif arr[mid]>=target:
                r=mid-1
            else:
                l=mid+1
        
        if start==-1:
            return [-1,-1]
        
        # Binary Search to find Last Position
        l,r = 0,n-1
        while l<=r:
            if l==r:
                if arr[l]==target:
                    end=l
                break
            if l==r-1:
                if arr[r]==target:
                    end=r
                elif arr[l]==target:
                    end=l
                break
            mid=(l+r)//2
            if arr[mid]==target and arr[mid+1]>target:
                end=mid
                break
            elif arr[mid]<=target:
                l=mid+1
            else:
                r=mid-1
                
        return [start,end]
       