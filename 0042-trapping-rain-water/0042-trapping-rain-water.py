class Solution:
    def trap(self, height: List[int]) -> int:
        
        n=len(height)
        left,right=0,n-1
        leftMax=height[0]
        rightMax=height[n-1]
        
        water=0
        
        while left<right:
            if height[left]<height[right]:
                if height[left]>leftMax:
                    leftMax=height[left]
                else:
                    water+=leftMax-height[left]
                left+=1
            else:
                if height[right]>rightMax:
                    rightMax=height[right]
                else:
                    water+=rightMax-height[right]
                right-=1
        
        return water
                