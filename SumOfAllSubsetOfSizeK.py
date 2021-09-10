
from math import factorial as fact
def ncr(n,r):
    return fact(n)//(fact(r)*fact(n-r))

def main():
    arr=list(map(int,input().split()))
    k=int(input())
    
    val=ncr(len(arr)-1,k-1)
    
    
    print(sum(arr)*val)
    
    
    
    
    
    
    
    
    
    
    
    
    
main()
            
