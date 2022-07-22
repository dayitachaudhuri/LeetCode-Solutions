class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # Defining adjacency list
        adj=[[] for i in range(0,numCourses)]
        indegree=[0]*numCourses
        for pair in prerequisites:
            indegree[pair[0]]+=1
            adj[pair[1]].append(pair[0])
        courses=[]
        openCourses=[node for node in range(0,numCourses) if indegree[node]==0]
        while openCourses:
            currCourse=openCourses.pop()
            courses.append(currCourse)
            indegree[currCourse]=-1
            for c in adj[currCourse]:
                indegree[c]-=1
                if indegree[c]==0:
                    openCourses.append(c)
        if len(courses)==numCourses:
            return courses
        else:
            return []