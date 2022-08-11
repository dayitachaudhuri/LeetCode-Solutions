class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def possible(capacity):
            curr, d = 0,0
            for wt in weights:
                if curr + wt > capacity:
                    d += 1
                    curr = 0
                curr += wt
            if curr > 0:
                d += 1
            return d
        
        maxWeight, sumWeight = 0,0
        for wt in weights:
            if wt > maxWeight:
                maxWeight = wt
            sumWeight += wt
        
        left = maxWeight
        right = sumWeight
        
        while left <= right:
            mid = (left + right) // 2
            req = possible(mid)
            if req > days:
                left = mid + 1
            else:
                right = mid - 1
        
        return left
                    