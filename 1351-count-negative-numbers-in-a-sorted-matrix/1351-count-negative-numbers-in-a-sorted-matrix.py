class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=0
        def find(start, end, lst):
            mid = (start + end)//2
            num = lst[mid]
            if num < 0 and (mid == 0 or lst[mid-1] >= 0):
                return mid
            if start >= end-1:
                if lst[end] < 0:
                    return end
                return end+1
            if num >= 0:
                return find(mid, end, lst)
            else:
                return find(start, mid, lst)
        if len(grid)==0 or len(grid[0])==0:
            return 0
        for i in range(0,len(grid)):
            first=find(0,len(grid[i])-1, grid[i])
            count+=len(grid[i])-first
        return count