class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        # Creating the Adjacency Table
        adj=defaultdict(lambda:[])
        for pair in edges:
            adj[pair[0]].append(pair[1])
            adj[pair[1]].append(pair[0])
            
        # Visiting all reachable nodes  
        visited={}
        def dfs(node):
            visited[node]=1
            for nextNode in adj[node]:
                if nextNode not in visited:
                    dfs(nextNode)
        
        dfs(source)
        
        # If destination is reached - 
        if destination in visited:
            return True
        else:
            return False
            