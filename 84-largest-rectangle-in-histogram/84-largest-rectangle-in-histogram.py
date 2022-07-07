class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        nex=[-1]*n
        prev=[-1]*n
        stack=[]
        for i in range(n-1,-1,-1):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if len(stack)==0:
                nex[i]=n
            else:
                nex[i]=stack[-1]
            stack.append(i)
        stack=[]
        for i in range(0,n):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if len(stack)==0:
                prev[i]=-1
            else:
                prev[i]=stack[-1]
            stack.append(i)
        area=0
        for i in range(0,n):
            currArea=heights[i]*(nex[i]-prev[i]-1)
            if currArea>area:
                area=currArea
        return area