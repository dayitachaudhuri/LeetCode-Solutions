class Solution:
    def trap(self, heights: List[int]) -> int:
        
        n=len(heights)
        
        # Define Left and Right Limit Arrays
        left=[0]*n
        right=[0]*n
        left[0]=heights[0]
        right[n-1]=heights[n-1]
        
        # Find Left and Right Limits
        for i in range(1,n):
            left[i]=max(left[i-1],heights[i])
            right[n-1-i]=max(right[n-i],heights[n-1-i])
             
        # Find Volume of water at each index
        water=0
        for i in range(0,n):
            water+=min(left[i],right[i])-heights[i]
        return water