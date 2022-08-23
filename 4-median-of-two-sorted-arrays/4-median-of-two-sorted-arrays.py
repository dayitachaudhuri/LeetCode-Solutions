class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        n=len(nums1)
        m=len(nums2)
        count=0
        i,j=0,0
        arr=[]
        
        while j<m and i<n:
            if nums1[i]>nums2[j]:
                arr.append(nums2[j])
                j+=1
            else:
                arr.append(nums1[i])
                i+=1
        
        while j<m:
            arr.append(nums2[j])
            j+=1
        
        while i<n:
            arr.append(nums1[i])
            i+=1
        
        if (n+m)%2==0:
            return (arr[(n+m)//2]+arr[(n+m)//2-1])/2
        return arr[(n+m)//2]