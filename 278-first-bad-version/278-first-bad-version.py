# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l,r = 1,n
        while l<=r:
            if l==r:
                return l
            if l==r-1:
                if isBadVersion(l)==True:
                    return l
                return r
            mid=(l+r)//2
            bad=isBadVersion(mid)
            prev=isBadVersion(mid-1)
            if bad and not prev:
                return mid
            if bad:
                r=mid-1
            else:
                l=mid+1
    