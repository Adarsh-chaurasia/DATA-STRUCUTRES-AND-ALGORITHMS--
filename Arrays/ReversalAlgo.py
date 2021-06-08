def reverse(arr,s,e):
  while s<e:
    temp=arr[s]
    arr[s]=arr[e]
    arr[e]=temp
    s+=1
    e-=1


def main():
  arr=[1,2,3,4,5,6,7]
  n=7
  d=2
  reverse(arr,0,d-1)
  reverse(arr,d,n-1)
  reverse(arr,0,n-1)
