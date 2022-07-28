class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        sortedWords=["".join(sorted(i)) for i in words]
        ans=[words[0]]
        prev=0
        for i in range(1,len(words)):
            if sortedWords[i]!=sortedWords[prev]:
                prev=i
                ans.append(words[i])
        return ans