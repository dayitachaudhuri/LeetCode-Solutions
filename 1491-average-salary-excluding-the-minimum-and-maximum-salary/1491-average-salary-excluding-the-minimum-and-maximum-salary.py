class Solution:
    def average(self, salary: List[int]) -> float:
        if len(salary)<=2:
            return 0
        minSal=min(salary[0],salary[1])
        maxSal=max(salary[0],salary[1])
        tot=0
        for sal in salary[2:]:
            if sal>maxSal:
                tot+=maxSal
                maxSal=sal
            elif sal<minSal:
                tot+=minSal
                minSal=sal
            else:
                tot+=sal
        return tot/(len(salary)-2)