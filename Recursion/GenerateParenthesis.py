def solve(o,c,op,list1=[]):
    if o==0 and c==0:
        list1.append(op)
        
    
    if o!=0:
        op1=op
        op1+="("
        solve(o-1,c,op1,list1)
    if c>o:
        op2=op
        op2+=")"
        solve(o,c-1,op2,list1)

class Solution:
    def AllParenthesis(self,n):
        open=n
        close=n
        output=""
        list1=[]
        
        solve(open,close,output,list1)
        
        return list1
