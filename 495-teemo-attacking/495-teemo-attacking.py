class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        tot=0
        start=timeSeries[0]
        end=timeSeries[0]+duration
        for i in range(1,len(timeSeries)):
            if timeSeries[i]>end:
                tot+=end-start
                start=timeSeries[i]
                end=timeSeries[i]+duration
            else:
                end=timeSeries[i]+duration
        tot+=end-start
        return tot