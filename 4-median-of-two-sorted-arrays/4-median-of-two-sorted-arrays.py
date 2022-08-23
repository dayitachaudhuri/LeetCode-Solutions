class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n=len(nums1)
        m=len(nums2)
        count=0
        i,j=0,0
        curr=0
        prev=0
        
        while count<=(n+m)//2 and j<m and i<n:
            prev=curr
            if nums1[i]>nums2[j]:
                curr=nums2[j]
                j+=1
            else:
                curr=nums1[i]
                i+=1
            count+=1
            
        if count<=(n+m)//2:
            prev=curr
            if j<m:
                j+=(n+m)//2-count
                curr=nums2[j]
                if j!=0:
                    prev=max(prev,nums2[j-1])
            else:
                i+=(n+m)//2-count
                curr=nums1[i]
                if i!=0:
                    prev=max(prev,nums1[i-1])
        
        if (n+m)%2==0:
            curr=(curr+prev)/2
        return curr