class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l,r  = 0,len(nums)
        flag = False
        while(l<=r and l<len(nums) and r>=0):
            m = (l+r)//2
            if nums[m] > target:
                r = m-1
            elif nums[m] < target:
                l = m+1
            else:
                flag = True
                break
        if flag == False:
            return [-1,-1]
        else:
            l,r = m,m
            while(True):
                if l != 0 and nums[l-1] == target:
                    l -= 1
                else:
                    break
            while(True):
                if r != len(nums)-1 and nums[r+1] == target:
                    r += 1
                else:
                    break
        return [l,r]