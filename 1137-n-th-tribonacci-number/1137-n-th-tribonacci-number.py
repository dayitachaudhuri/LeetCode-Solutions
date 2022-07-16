class Solution:
    def tribonacci(self, n: int) -> int:
        prev3,prev2,prev1=0,1,1
        if n<=1:
            return n
        if n==2:
            return 1
        for i in range(0,n-2):
            curr=prev1+prev2+prev3
            prev3=prev2
            prev2=prev1
            prev1=curr
        return prev1