n=6
edges=[[1,2],[1,3],[2,3],[2,4],[3,4]]

graph=dict()

for i in range(1,n+1):
  graph[i]=[]
  
  
for i,j in edges:
  graph[i].append(j)
  graph[j].append(i)
  
  
  
  
for u,v in graph.items():
  print(u,"->",v)
