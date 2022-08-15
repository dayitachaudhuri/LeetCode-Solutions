class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        # Function to Calculate Number of Days
        
        def calculateDays(capacity):
            d, curr = 0, 0
            for w in weights:
                # If weight exceeds capacity
                if curr + w > capacity:
                    d += 1
                    curr = 0
                curr += w
            # If weight remains
            if curr > 0:
                d+=1
            return d
        
        # Find left and right extremes
        
        left, right = 0, 0
        for w in weights:
            if w > left:
                left = w
            right += w
            
        # Binary Search
        
        while left <= right:
            
            mid = (left + right) // 2
            
            # If days is exceeding given limit, increase the chosen capacity.
            if calculateDays(mid)>days:
                left = mid + 1
            
            # If days is less than given limit, decrease the chosen capacity.
            else:
                right = mid - 1
        
        # Final value of left at which we exit the loop is the solution
        return left