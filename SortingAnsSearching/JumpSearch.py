import math
def jumpSearch(arr,n,x):
    m= math.sqrt(n)
    prev = 0
    while arr[int(min(m, n)-1)] < x:
        prev = m
        m += math.sqrt(n)
        if prev >= n:
    
            return -1
            
    while arr[int(prev)] < x:
        prev += 1
             
        if prev == min(m, n):
            return -1
    if arr[int(prev)] == x:
        return int(prev)
         
    return -1
    
    
print(jumpSearch([1,2,3,4,5,6,7,8,9],9,4))
