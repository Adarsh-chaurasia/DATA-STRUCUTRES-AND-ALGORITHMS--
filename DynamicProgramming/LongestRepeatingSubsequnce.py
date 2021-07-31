def lrs(a):
    n=len(a)
    dp=[[0 for i in range(n+1)]for j in range(n+1)]
    
    for i in range(1,n+1):
        for j in range(1,n+1):
            if ((a[i-1]==a[j-1]) and i!=j):
                dp[i][j]=1+dp[i-1][j-1]
                
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
                
                
    return dp[n][n]
class Solution:
	def LongestRepeatingSubsequence(self, str):
		return lrs(str)
