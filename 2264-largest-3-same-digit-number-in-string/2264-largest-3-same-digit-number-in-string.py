class Solution:
    def largestGoodInteger(self, num: str) -> str:
        lst=[0]*10
        count=0
        maxVal=""
        for i in range(1,len(num)):
            if num[i]==num[i-1]:
                count+=1
            else:
                count=0
            if count==2:
                if maxVal=="" or int(num[i]*3)>int(maxVal):
                    maxVal=num[i]*3

        return maxVal