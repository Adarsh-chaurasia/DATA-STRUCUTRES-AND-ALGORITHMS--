def dfs(start,graph,visited,output):
    visited[start]=True
    output.append(start)
    for next in graph[start]:
        if not visited[next]:
            dfs(next,graph,visited,output)
            
    return output

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        visited=[False]*V
        output=[]
        return dfs(0,adj,visited,output)
        
