

def lcs(x,y,m,n):
    dp=[[0 for j in range(n+1)] for i in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if x[i-1]==y[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i][j-1],dp[i-1][j])
                
    return dp[m][n]
    
    
def main():
    str1=input()
    m=len(str1)
    str2="abcdefghijklmnopqrstuvwxyz"
    n=len(str2)
    
    res=lcs(str1,str2,m,n)
    
    print(n-res)
    
main()
