class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        flag=0
        incr=0
        decr=0
        if len(arr)<3:
            return False
        for i in range(0,len(arr)-1):
            if arr[i]<arr[i+1]:
                if flag==1:
                    return False
                incr+=1
            elif arr[i]==arr[i+1]:
                return False
            else:
                flag=1
                decr+=1
        if incr==0 or decr==0:
            return False
        return True
                