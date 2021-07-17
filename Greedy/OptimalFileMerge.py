import heapq
file=list(map(int,input().split()))

heapq.heapify(file)

cost=0
while len(file)>1:
    a=heapq.heappop(file)
    b=heapq.heappop(file)
    cost+=a+b
    heapq.heappush(file,a+b)
    
    
print(cost)
