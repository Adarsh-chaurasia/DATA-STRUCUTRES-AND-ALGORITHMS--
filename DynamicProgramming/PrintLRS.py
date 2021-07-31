def longestRepeatingSubsequence(a):
    m=len(a)
    dp=[[0 for i in range(m+1)]for j in range(m+1)]
    
    for i in range(1,m+1):
        for j in range(1,m+1):
            if a[i-1]==a[j-1] and i!=j:
                dp[i][j]=1+dp[i-1][j-1]
                
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
                
                
    i=m
    j=m
    s=" "
    
    while i>0 and j>0:
        if a[i-1]==a[j-1] and i!=j:
            s+=a[i-1]
            i-=1
            j-=1
            
        else:
            if dp[i-1][j]>dp[i][j-1]:
                i-=1
            else:
                j-=1
                
    return "".join(reversed(s))
    
    
    
def main():
    s="banana"
    
    res=longestRepeatingSubsequence(s)
    
    print(res)
    
main()
