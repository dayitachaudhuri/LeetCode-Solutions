class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj,count=0,0
        for i in nums:
            if count==0:
                maj=i
            if i==maj:
                count+=1
            else:
                count-=1
        return maj