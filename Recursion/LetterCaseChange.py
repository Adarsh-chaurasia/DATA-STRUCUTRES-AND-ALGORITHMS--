def caseChange(ip,op,list=[]):
    if len(ip)==0:
        list.append(op)
        return
    if ip[0].isalpha():
        op1=op
        op2=op
        op1+=ip[0].upper()
        op2+=ip[0].lower()
        ip=ip[1:]
        
        caseChange(ip,op1,list)
        caseChange(ip,op2,list)
        
    else:
        op1=op
        op1+=ip[0]
        ip=ip[1:]
        caseChange(ip,op1,list)
        
    return
    

    
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        output=""
        list=[]
        caseChange(s,output,list)
        return list
