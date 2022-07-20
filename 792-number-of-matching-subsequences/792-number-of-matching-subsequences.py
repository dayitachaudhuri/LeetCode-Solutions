class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        bucket=defaultdict(lambda:[])
        count=0
        for word in words:
            bucket[word[0]].append(word)
            
        for char in s:
            for i in range(0,len(bucket[char])):
                word=bucket[char].pop(0)
                if len(word)<=1:
                    count+=1
                else:
                    bucket[word[1]].append(word[1:])
        return count