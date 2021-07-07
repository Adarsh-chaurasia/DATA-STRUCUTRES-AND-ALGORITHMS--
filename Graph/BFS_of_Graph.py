class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        visited = [False] * (V + 1)
        queue = []
        queue.append(0)
        visited[0] = True
        output=[]
        while queue:
            s = queue.pop(0)
            output.append(s)
            for i in adj[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
        return output
