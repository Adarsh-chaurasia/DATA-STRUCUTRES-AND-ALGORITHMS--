def getNth(head, k):
    ptr=head
    
    while k>1:
        ptr=ptr.next
        k-=1
        
    return ptr.data
