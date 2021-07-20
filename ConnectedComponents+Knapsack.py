def dfs(node,temp,graph,visited):
    temp.append(node)
    visited[node]=True
    for friends in graph[node]:
        if not visited[friends]:
            dfs(friends,temp,graph,visited)
            

def knapsack(W,val,wt,n):
    dp=[[0 for i in range(W+1)] for j in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,W+1):
            if wt[i-1]<=j:
                dp[i][j]=max(val[i-1]+dp[i-1][j-wt[i-1]],dp[i-1][j])
            else:
                dp[i][j]=dp[i-1][j]
                
    return dp[n][W]
    
def main():
    n , a = map(int,input().split())
    skillSet=[]
    for i in range(n):
        pairs=list(map(int,input().split()))
        skillSet.append(pairs)
        
    graph=dict()
    for i in range(1,n+1):
        graph[i]=[]
    q , b = map(int,input().split())
    for _ in range(q):
        u,v=map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
        
    budget=int(input())
    
    groupOfEmp=[]
    visited=[False]*(n+1)
    for emp in range(1,n+1):
        if visited[emp] is not True:
            group=[]
            dfs(emp,group,graph,visited)
            groupOfEmp.append(group)
    length=len(groupOfEmp)
    skills=[0]*length
    cost=[0]*length
    i=0
    for each in groupOfEmp:
        for j in each:
            sk,sal=skillSet[j-1]
            skills[i]+=sk
            cost[i]+=sal
        i+=1
        
    ans=knapsack(budget,skills,cost,length)
    print(ans)

main()
