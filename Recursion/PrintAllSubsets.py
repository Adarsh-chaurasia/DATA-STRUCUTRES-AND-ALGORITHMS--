def subsets(ip,op,list):
    if len(ip)==0:
        list.append(op)
        return
    op1=op
    op2=op
    
    op2+=ip[0]
    ip=ip[1:]
    
    subsets(ip,op1,list)
    subsets(ip,op2,list)
    
    return







def main():
    string=input()
    output=" "
    list=[]
    subsets(string,output,list)
    print(list)
    
main()
