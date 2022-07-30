class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        maxSize=1
        i=0
        j=1
        dic={s[0]:0}
        while j<len(s):
            if s[j] in dic and dic[s[j]]>=i:
                i=dic[s[j]]+1
            if j-i+1>maxSize:
                maxSize=j-i+1
            dic[s[j]]=j
            j+=1
        return maxSize