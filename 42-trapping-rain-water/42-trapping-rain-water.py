class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        if n<2:
            return 0
        water=0
        l=height[0]
        left=[0]*n
        for i in range(0,n):
            if height[i]>l:
                l=height[i]
            left[i]=l
        r=height[-1]    
        right=[0]*n
        for i in range(n-1,-1,-1):
            if height[i]>r:
                r=height[i]
            right[i]=r
        for i in range(1,n-1):
            if left[i]>height[i] and right[i]>height[i]:
                water+=min(left[i],right[i])-height[i]
        return water