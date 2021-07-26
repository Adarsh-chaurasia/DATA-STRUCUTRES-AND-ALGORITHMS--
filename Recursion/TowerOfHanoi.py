def toh(n,src,aux,dest):
    if n==1:
        print("Move disk",n," from rod",src,"to rod",dest)
        return
    toh(n-1,src,dest,aux)
    print("Move disk",n," from rod",src,"to rod",dest)
    toh(n-1,aux,src,dest)

def main():
    n=int(input())
    
    toh(n,"A","B","C")
main()
