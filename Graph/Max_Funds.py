def dfs(temp,node,graph,visited):
    temp.append(node)
    visited[node]=True
    
    for n in graph[node]:
        if visited[n] is not True:
            temp=dfs(temp,n,graph,visited)
            
    return temp

def main():
    n=int(input())
    array=list(map(int,input().split()))
    graph=dict()
    for i in range(1,n+1):
        graph[i]=[]
        
    edges=int(input())    
    for i in range(edges):
        u,v=input().split()
        graph[int(u)].append(int(v))
        graph[int(v)].append(int(u))
        
        
    visited=[False]*(n+1)
    components=[]
    for i in range(1,n+1):
        if len(graph[i])>0 and visited[i] is not True:
            temp=[]
            components.append(dfs(temp,i,graph,visited))
        elif len(graph[i])==0:
            components.append([i])
            
            
    max_fund=0
    for each in components:
        total=0
        for i in each:
            total+=array[i-1]
        max_fund=max(max_fund,total)
        
    print(max_fund)
    
main()
