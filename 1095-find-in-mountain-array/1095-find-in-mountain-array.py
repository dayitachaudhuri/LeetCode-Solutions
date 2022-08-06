# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        
        # Find Peak
        n=mountain_arr.length()
        l, r = 0, n-1
        peak=0     
        while l<=r:
            
            mid=(l+r)//2
            val=mountain_arr.get(mid)
            # If mid is in slope up
            if mid==0 or (mid!=n-1 and val<mountain_arr.get(mid+1)):
                l=mid+1
            
            # If mid is in slope down
            elif mid==n-1 or (mid!=0 and val<mountain_arr.get(mid-1)):
                r=mid-1
                
            # If mid is peak
            else:
                peak=mid
                break
        
        if mountain_arr.get(peak)==target:
            return mid
        
        # Search in Increasing Subarray
        l, r = 0, peak-1
             
        while l<=r:
            mid=(l+r)//2
            val=mountain_arr.get(mid)
            if val==target:
                return mid
            elif val>target:
                r=mid-1
            else:
                l=mid+1
                
        # Search in Decreasing Subarray
        l, r = peak+1, n-1
             
        while l<=r:
            mid=(l+r)//2
            val=mountain_arr.get(mid)
            if val==target:
                return mid
            elif val<target:
                r=mid-1
            else:
                l=mid+1
        
        return -1