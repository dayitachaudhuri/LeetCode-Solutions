class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        for b in range(0,n):
            a=0
            while a<m+b:
                if nums1[a]>nums2[b]:
                    nums1[a],nums2[b]=nums2[b],nums1[a]
                a+=1 
            nums1[a]=nums2[b]
        