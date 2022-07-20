class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        bucket={}
        count=0
        for word in words:
            if word[0] in bucket:
                bucket[word[0]].append(word)
            else:
                bucket[word[0]]=[word]
        for char in s:
            if char in bucket:
                for i in range(0,len(bucket[char])):
                    word=bucket[char].pop(0)
                    if len(word)<=1:
                        count+=1
                    else:
                        if word[1] in bucket:
                            bucket[word[1]].append(word[1:])
                        else:
                             bucket[word[1]]=[word[1:]]
        return count