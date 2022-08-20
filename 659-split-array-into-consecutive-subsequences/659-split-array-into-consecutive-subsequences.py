class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        splits = [[nums[0]]]
        currow = 0
        level = nums[0]
        for a in nums[1:]:
            if splits[currow][-1] + 1 == a:
                if currow < len(splits) - 1:
                    currow = len(splits) - 1
                splits[currow].append(a)
            elif splits[currow][-1] == a:
                if not currow:
                    splits.append([a])
                    currow = len(splits) - 1
                else:
                    if splits[currow-1][-1] + 1 == a:
                        currow -= 1
                        splits[currow].append(a)
                    else:
                        splits.append([a])
                        currow = len(splits) - 1
            else:
                splits.append([a])
                currow = len(splits) -1
        return min(len(e) for e in splits) >= 3