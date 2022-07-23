class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj=[[] for i in range(0,numCourses)]
        indegree=[0 for i in range(0,numCourses)]
        visited=[0 for i in range(0,numCourses)]
        rec=[0 for i in range(0,numCourses)]
        for pair in prerequisites:
            adj[pair[1]].append(pair[0])
            indegree[pair[0]]+=1
        def dfs(node, rec):
            visited[node]=1
            rec[node]=1
            for nextNode in adj[node]:
                if  visited[nextNode]==0:
                    if dfs(nextNode, rec):
                        return True
                elif rec[nextNode]==1:
                    return True
            rec[node]=0
            return False
        for course in range(0,numCourses):
            if visited[course]==0 and dfs(course,rec):
                return False
        return True
                    