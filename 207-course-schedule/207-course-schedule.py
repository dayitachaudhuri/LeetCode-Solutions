class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n=numCourses
        adj=[[] for i in range(0,n)]
        indegree=[0]*n
        for pair in prerequisites:
            indegree[pair[0]]+=1
            adj[pair[1]].append(pair[0])
        courses=[]
        ans=True
        while ans:
            ans=False
            for i in range(0,n):
                if indegree[i]==0:
                    courses.append(i)
                    indegree[i]=-1
                    for vertex in adj[i]:
                        indegree[vertex]-=1
                    ans=True
                    break
        if len(courses)==n:
            return True
        else:
            return False
                    