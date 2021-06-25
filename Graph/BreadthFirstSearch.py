from collections import deque

def bfsSearch(graph,start,n):
    queue=deque([])
    visited=[False]*(n+1)
    bfs=[]
    
    queue.append(start)
    visited[start]=True
    
    while queue:
        current=queue.popleft()
        bfs.append(current)
        
        for each in graph[current]:
            if visited[each] is not True:
                queue.append(each)
                visited[each]=True
                
    return bfs

n, e = tuple(map(int,input().split())) 
graph=dict()

for i in range(1,n+1):
  graph[i]=[]
  
  
for _ in range(e):
    u,v =tuple(map(int,input().split())) 
    graph[u].append(v)
    graph[v].append(u)
  
  
  
ans=bfsSearch(graph,3,n)
  
print(*ans)
