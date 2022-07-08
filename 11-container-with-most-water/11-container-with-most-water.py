class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        n=len(height)
        left,right=0,n-1
        maxWater=0
        
        while left<right:
            
            # If left is less, increment left.
            if height[left]<height[right]:
                water=height[left]*(right-left)
                left+=1
                
            # If right is less, decreement right.
            else:
                water=height[right]*(right-left)
                right-=1
                
            # Update water.
            if water>maxWater:
                maxWater=water
        
        return maxWater