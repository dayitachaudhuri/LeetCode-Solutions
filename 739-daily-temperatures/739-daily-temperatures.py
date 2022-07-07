class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    
        n=len(temperatures)
        answer=[0]*n
        stack=[]
        
        # Find index of NGE for each element.
        for i in range(n-1,-1,-1):
            
            while stack and temperatures[stack[-1]]<=temperatures[i]:
                stack.pop()
            if stack:
                # Find no. of days by calculating distance between current index and index of NGE
                answer[i]=stack[-1]-i
                
            stack.append(i)
            
        return answer