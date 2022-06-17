class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        last = -duration
        res = 0
        for time in timeSeries:
            if time - last < duration:
                res -= last + duration - time
            res += duration
            last = time
        return res