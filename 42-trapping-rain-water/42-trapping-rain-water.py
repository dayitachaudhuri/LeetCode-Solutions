class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        if n<2:
            return 0
        water=0
        leftMax,rightMax=0,0
        l,r=0,n-1
        while l<=r:
            if height[l]<=height[r]:
                if height[l]>leftMax:
                    leftMax=height[l]
                else:
                    water+=leftMax-height[l]
                l+=1
            else:
                if height[r]>rightMax:
                    rightMax=height[r]
                else:
                    water+=rightMax-height[r]
                r-=1
        return water
        