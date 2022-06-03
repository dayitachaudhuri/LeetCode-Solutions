class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj,count=0,0
        for i in nums:   
            if i==maj:
                count+=1
            elif count==0:
                maj=i
                count=1
            else:
                count-=1
        return maj