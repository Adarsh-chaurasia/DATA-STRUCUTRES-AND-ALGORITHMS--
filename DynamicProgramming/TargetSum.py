def countSubset(arr,n,s):
    dp=[[0 for i in range(s+1)]for j in range(n+1)]
    
    for i in range(n+1):
        dp[i][0]=1
        
    for i in range(1,n+1):
        for j in range(1,s+1):
            if arr[i-1]<=j:
                dp[i][j]=dp[i-1][j]+dp[i-1][j-arr[i-1]]
                
            else:
                dp[i][j]=dp[i-1][j]
                
    return dp[n][s]
class Solution:
    def findTargetSumWays(self, arr, N, target):
        s=sum(arr)
        sum1=(target+s)//2
        if s< target or (s + target)%2 != 0 :
            return 0
        
        result=countSubset(arr,N,sum1)
        
        return result
