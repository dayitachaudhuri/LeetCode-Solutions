class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        # Creating the Adjacency Table
        
        adj=defaultdict(lambda:[])
        for pair in edges:
            adj[pair[0]].append(pair[1])
            adj[pair[1]].append(pair[0])
            
            
        visited={}
        def dfs(node):
            if node==destination:
                return True
            visited[node]=1
            for nextNode in adj[node]:
                if nextNode not in visited:
                    if dfs(nextNode):
                        return True
            return False
        
        return dfs(source)
            