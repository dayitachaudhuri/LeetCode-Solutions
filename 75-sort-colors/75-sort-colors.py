class Solution:
    def sortColors(self, nums: List[int]) -> None:
        r,w,b=0,0,0
        for i in nums:
            if i==0:
                r+=1
            elif i==1:
                w+=1
            elif i==2:
                b+=1
        for i in range(0,r):
            nums[i]=0
        for i in range(r,w+r):
            nums[i]=1
        for i in range(w+r,b+w+r):
            nums[i]=2