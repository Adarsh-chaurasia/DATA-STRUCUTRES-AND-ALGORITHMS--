def reverse(arr,s,e):
    while s<e:
        arr[s],arr[e]=arr[e],arr[s]
        s+=1
        e-=1

class Solution:
    def rotate(self, arr: List[int], d: int) -> None:
        if d==0:
            return
        n=len(arr)
        d=d%n
        
        reverse(arr,0,n-1)
        reverse(arr,0,d-1)
        reverse(arr,d,n-1)
