#User function Template for python3

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        # code here
        time=[]
        i,j=0,0
        arr.sort()
        dep.sort()
        while i<len(arr) and j<len(dep):
            if dep[j]<arr[i]:
                time.append(-1)
                j+=1
            else:
                time.append(1)
                i+=1
        while j<len(dep):
            time.append(-1)
            j+=1
        while i<len(arr):
            time.append(1)
            i+=1
        maxcount=0
        count=0
        for value in time:
            count+=value
            if count>maxcount:
                maxcount=count
        if count>maxcount:
            maxcount=count
        return maxcount

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        arrival = list(map(int, input().strip().split()))
        departure = list(map(int, input().strip().split()))
        ob=Solution()
        print(ob.minimumPlatform(n,arrival,departure))
# } Driver Code Ends