class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        tot=duration
        for i in range(0,len(timeSeries)-1):
            if timeSeries[i+1]-timeSeries[i]<duration:
                tot+=timeSeries[i+1]-timeSeries[i]
            else:
                tot+=duration
        return tot