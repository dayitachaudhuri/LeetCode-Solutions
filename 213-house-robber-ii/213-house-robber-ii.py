class Solution:
    def rob(self, arr: List[int]) -> int:
        
        def findmax(k,n):
            if n==k+1:
                return arr[k]
            prev2=arr[k]
            prev1=max(arr[k],arr[k+1])
            for i in range(k+2,n):
                curr=max(arr[i]+prev2,prev1)
                prev2=prev1
                prev1=curr
            return prev1
        
        if len(arr)==1:
            return arr[0]
        
        return max(findmax(0,len(arr)-1),findmax(1,len(arr)))