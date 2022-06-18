class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        count=0
        for i in range(0,len(colors)-1):
            if colors[i]==colors[i+1]:
                count+=min(neededTime[i],neededTime[i+1])
                neededTime[i+1]=max(neededTime[i],neededTime[i+1])
        return count