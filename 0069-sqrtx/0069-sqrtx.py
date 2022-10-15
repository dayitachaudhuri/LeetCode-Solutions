class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0 or x==1:
            return x
        l=0
        r=x
        while l<=r:
            mid=(l+r)//2
            if mid**2==x:
                return mid
            if mid**2>x:
                r=mid-1
            else:
                l=mid+1
        return min(l,r)
            