class Solution:
    def trap(self, height: List[int]) -> int:
        
        n=len(height)
        left,right=0,0
        leftMax=[0]*n
        rightMax=[0]*n
        
        for i in range(0,n):
            leftMax[i]=left
            left=max(left,height[i])
            
        for i in range(n-1,-1,-1):
            rightMax[i]=right
            right=max(right,height[i])
            
        water=0
        for i in range(1,n-1):
            a=min(leftMax[i],rightMax[i])
            if a>height[i]:
                water+=a-height[i]
                
        return water