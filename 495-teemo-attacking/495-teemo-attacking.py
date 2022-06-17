class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        tot=0
        prev=-duration
        for curr in timeSeries:
            if curr-prev<duration:
                tot+=curr-prev
            else:
                tot+=duration
            prev=curr
        return tot