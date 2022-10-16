class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        # Function to Calculate Number of Days
        def findDays(capacity):
            curr=0
            d=1
            for wt in weights:
                if curr+wt>capacity:
                    d+=1
                    curr=wt
                else:
                    curr+=wt
            return d
        
        
        # Find left and right extremes
        left,right=weights[0],0
        for wt in weights:
            if wt>left:
                left=wt
            right+=wt
            
        # Binary Search
        while left<right:
            mid=(left+right)//2
            if findDays(mid)>days:
                left=mid+1
            else:
                right=mid
        return left