class Solution:
    def longestCommonSubstr(self, S1, S2, n, m):
        dp=[[0 for i in range(m+1)]for i in range(n+1)]
        result=0
        for i in range(1,n+1):
            for j in range(1,m+1):
                if S1[i-1]==S2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                    result=max(result,dp[i][j])
                else:
                    dp[i][j]=0
                    
                    
        return result
