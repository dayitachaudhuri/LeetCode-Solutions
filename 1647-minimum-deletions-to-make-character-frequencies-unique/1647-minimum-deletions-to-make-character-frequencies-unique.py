class Solution:
    def minDeletions(self, s: str) -> int:
        cache={}
        for i in s:
            if i in cache:
                cache[i]+=1
            else:
                cache[i]=1
        count=0
        freq_set=list(cache.values())
        i=0
        while i<len(freq_set):
            if freq_set[i]!=0 and freq_set[i] in freq_set[:i]:
                freq_set[i]-=1
                count+=1
            else:
                i+=1
        return count