def Push(x,s1,s2):
    s1.append(x)


def Pop(s1,s2):
    if len(s1) == 0 and len(s2) == 0:
            return -1
 
       
    elif len(s2) == 0 and len(s1) > 0:
        while len(s1):
            temp = s1.pop()
            s2.append(temp)
        return s2.pop()
    else:
        return s2.pop()
    
