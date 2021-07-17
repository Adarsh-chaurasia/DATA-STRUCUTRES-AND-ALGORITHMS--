def binarySearch(arr,low,high,target):
    while low<high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]>target:
            return binarySearch(arr,low,mid-1,target)
            
        else:
            return binarySearch(arr,mid+1,high,target)

def exponentialSearch(arr,n,x):
    if arr[0]==x:
        return 0
        
    i=1
    while i<n and arr[i]<=x:
        i=i*2
        
    return binarySearch(arr,i//2,min(i,n-1),x)
    
print("At Index :",exponentialSearch([1,2,3,4,5,6,7,8,9],9,4))
