class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        time=[-1]*n
        low=[-1]*n
        ans=[]
        
        adj=defaultdict(lambda:[])
        for pair in connections:
            adj[pair[0]].append(pair[1])
            adj[pair[1]].append(pair[0])
            
        def dfs(node, t, parent):
            time[node]=t
            low[node]=t
            for nextNode in adj[node]:
                if time[nextNode]==-1:
                    dfs(nextNode, t+1, node)
                    low[node]=min(low[node],low[nextNode])
                    if low[nextNode]>time[node]:
                        ans.append([node,nextNode])
                elif nextNode!=parent:
                    low[node]=min(low[node],time[nextNode])
                    
        dfs(0,0,None)
        return ans