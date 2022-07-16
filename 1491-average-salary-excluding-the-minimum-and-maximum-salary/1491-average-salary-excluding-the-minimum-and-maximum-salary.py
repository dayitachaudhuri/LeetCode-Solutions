class Solution:
    def average(self, salary: List[int]) -> float:
        minSal=99999999
        maxSal=0
        tot=0
        for sal in salary:
            if sal>maxSal:
                maxSal=sal
            if sal<minSal:
                minSal=sal
            tot+=sal
        return (tot-minSal-maxSal)/(len(salary)-2)