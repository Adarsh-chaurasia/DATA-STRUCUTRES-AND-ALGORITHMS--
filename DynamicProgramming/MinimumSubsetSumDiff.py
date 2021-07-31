def subsetSum (N, arr, sum):
        dp=[[False for i in range(sum + 1)]
            for i in range(N + 1)]
        for i in range(N+1):
            dp[i][0]=True
            
        for j in range(1,sum+1):
            dp[0][j]=False
                    
                    
        for i in range(1,N+1):
            for j in range(1,sum+1):
                if arr[i-1]<=j:
                    dp[i][j]=dp[i-1][j-arr[i-1]] or dp[i-1][j]
                    
                else:
                    dp[i][j]=dp[i-1][j]
                    
        return dp
class Solution:
	def minDifference(self, arr, n):
		sum_=sum(arr)
		matrix=subsetSum(n,arr,sum_)
		candi=[]
		for i in range(sum_//2+1):
		    if matrix[n][i]:
		        candi.append(i)
		min_=2147483647
        for i in range(len(candi)):
            min_=min(min_,(sum_-2*candi[i]))
        return(min_)
