class Solution:
    def findMaxAverage(self, Arr: List[int], k: int) -> float:
        
        currAv=0
        for i in range(0,k):
            currAv+=Arr[i]
        currAv/=k
        maxAv=currAv
        
        start,end=0,k
        while end<len(Arr):
            currAv=currAv-Arr[start]/k+Arr[end]/k
            if currAv>maxAv:
                maxAv=currAv
            start+=1
            end+=1
            
        return maxAv
