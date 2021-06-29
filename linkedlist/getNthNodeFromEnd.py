def getNthFromLast(head,n):
    count=length(head)
    k=count-n
    if k<0:
        return -1
    else:
        ptr=head
        for i in range(1,k+1):
            
            ptr=ptr.next
        return ptr.data
