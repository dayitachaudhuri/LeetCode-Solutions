class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def makePattern(w):
            d, a, count = {}, [], 0
            for c in w:
                if c not in d:
                    d[c] = count
                    count += 1
                a.append(d[c])
            return a
        p = makePattern(pattern)
        return [w for w in words if makePattern(w) == p]