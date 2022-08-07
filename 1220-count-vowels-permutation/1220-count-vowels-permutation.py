class Solution:
    def countVowelPermutation(self, n: int) -> int:
        go={"a":["e"],"e":["a","i"],"i":["a","e","o","u"],"o":["i","u"],"u":["a"]}
        dp={}
        def helper(curr, rem):
            if rem==0:
                return 1
            if (curr,rem) in dp:
                return dp[(curr,rem)]
            count=0
            for i in go[curr]:
                count+=helper(i,rem-1)
            dp[(curr,rem)]=count
            return count
        tot=0
        for val in go.keys():
            tot+=helper(val,n-1)
        return tot%(10**9+7)