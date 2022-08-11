class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        
        def bags(capacity, nums):
            count = 0
            for val in nums:
                if val <= capacity:
                    continue
                if val % capacity == 0:
                    count += val // capacity - 1
                else:
                    count += val // capacity
            return count
        
        left = 1
        right = 1
        for n in nums:
            if n > right:
                right = n
        
        while left <= right:
            mid = (left + right) // 2
            if bags(mid,nums) > maxOperations:
                left = mid+1
            else:
                right = mid-1
        return left