class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        low = [-1]*n
        distance = [-1]*n
        time = [0]
        par = [-1]*n
        bridges = []
        
        adj = defaultdict(list)
        
        for connection in connections:
            adj[connection[0]].append(connection[1]) 
            adj[connection[1]].append(connection[0]) 
        
        def dfs(curr):
            distance[curr]=low[curr]=time[0] 
            time[0]+=1
            for k in adj[curr]:
                if distance[k]==-1:
                    par[k]=curr
                    dfs(k)
                    low[curr]=min(low[curr], low[k])
                    
                    if low[k] > distance[curr]:
                        bridges.append([k, curr])
                        
                elif k!=par[curr]:                
                    low[curr] = min(low[curr], distance[k])
        
        for vertex in range(n):
            if distance[vertex]==-1:
                dfs(vertex)
        
        return bridges