class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        new=[intervals[0]]
        for i in intervals:
            if i[1]>new[-1][1]:
                if i[0]<=new[-1][1]:
                    new[-1][1]=i[1]
                else:
                    new.append(i)
        return new