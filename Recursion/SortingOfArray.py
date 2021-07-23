def insert(arr,x):
        n=len(arr)
        if len(arr)==0 or arr[n-1]<=x:
            arr.append(x)
            return
        val=arr.pop()
        insert(arr,x)
        arr.append(val)
        
        return
def sortArray(arr):
    
    
    if len(arr)==1:
        return
    temp=arr.pop()
    sortArray(arr)
    insert(arr,temp)
    
    
    
    

    
arr=   [2,3,7,6,4,5,9] 
sortArray(arr)
print(arr)
