def maxSubarraySum(arr, n) :
    max_far=arr[0]
    max_end=arr[0]
    for i in range(1,n):
        max_end+=arr[i]
        if max_end<0:
            max_end=0
        if max_far<max_end:
            max_far=max_end
            
    return max_far



