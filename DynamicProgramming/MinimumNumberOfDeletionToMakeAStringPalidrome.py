def lcs(x,y,n,m):
    dp=[[0 for j in range(m+1)]for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if x[i-1]==y[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp[n][m]


class Solution:
    def minimumNumberOfDeletions(self,S):
        t=S[::-1]
        m=len(S)
        n=len(t)
        res=lcs(S,t,m,n)
        
        return (m-res)
