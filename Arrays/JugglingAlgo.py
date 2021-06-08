def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
    

def leftRotation(arr,n,d):
    d=d%n
    x=gcd(n,d)
    for i in range(x):
        temp=arr[i]
        j=i
        while 1:
            k=j+d
           
            if k>=n:
                k-=n
            if k==i:
                break
            arr[j]=arr[k]
            j=k
        arr[j]=temp

    



arr=[1,2,3,4,5,6,7,8]
n=8
k=3
print(leftRotation(arr,n,k))
print(*arr)
