class Solution:
    
    def MAH(self,heights: List[int]) -> int:
        
        n=len(heights)
        
        # Next Lower Element Index for each i.
        right=[0]*n
        stack=[]
        for i in range(n-1,-1,-1):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if len(stack)==0:
                right[i]=n
            else:
                right[i]=stack[-1]
            stack.append(i)
        
        # Next Lower Element Index for each i.
        left=[0]*n
        stack=[]
        for i in range(0,n):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if len(stack)==0:
                left[i]=-1
            else:
                left[i]=stack[-1]
            stack.append(i)
            
        # Area for each heights[i].
        area=0
        for i in range(0,n):
            currArea=heights[i]*(right[i]-left[i]-1)
            if currArea>area:
                area=currArea
                
        return area
    
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        heights=[0]*len(matrix[0])
        maxArea=0
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                if matrix[i][j]=="0":
                    heights[j]=0
                else:
                    heights[j]+=1
            area=self.MAH(heights)
            print(area)
            if area>maxArea:
                maxArea=area
        return maxArea