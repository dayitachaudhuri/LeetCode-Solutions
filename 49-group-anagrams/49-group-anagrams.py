class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedStrs=["".join(sorted(i)) for i in strs]
        cache={}
        for i in range(0,len(sortedStrs)):
            if sortedStrs[i] in cache:
                cache[sortedStrs[i]].append(strs[i])
            else:
                cache[sortedStrs[i]]=[strs[i]]
        return list(cache.values())