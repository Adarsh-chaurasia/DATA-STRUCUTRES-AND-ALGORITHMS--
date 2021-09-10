def main():
    arr=list(map(int,input().split()))
    l,r,k=map(int,input().split())
    
    n=len(arr)
    d=dict()
    
    for each in arr:
        d[each]=d.get(each,0)+1
    flag=len(d)
    
    for i in range(l,r+1):
        if k==0 or flag>=n:
            break
        if d.get(i,0)!=0:
            continue
        else:
            flag+=1
            k-=1
            
            
    print(flag)
    
main()
