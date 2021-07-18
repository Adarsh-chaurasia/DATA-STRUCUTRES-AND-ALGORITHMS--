def lcs(x,y,n,m):
    if n==0 or m==0:
        return 0
    elif x[n-1]==y[m-1]:
        return 1+lcs(x,y,n-1,m-1)
    else:
        return max(lcs(x,y,n,m-1),lcs(x,y,n-1,m))
    
