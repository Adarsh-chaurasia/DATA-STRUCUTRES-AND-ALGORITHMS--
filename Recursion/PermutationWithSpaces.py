def subsets(ip,op,list=[]):
    if len(ip)==0:
        list.append(op)
        return
    op1=op
    op2=op
    op1+=" "
    op1+=ip[0]
    op2+=ip[0]
    ip=ip[1:]
    
    subsets(ip,op1,list)
    subsets(ip,op2,list)
    
    return

class Solution:
    def permutation (self, string):
        if len(string)==1:
            return [string]
        else:
            list=[]
            output=""
            output+=string[0]
            string=string[1:]
            subsets(string,output,list)
            #print(string,output)
            return(list)
