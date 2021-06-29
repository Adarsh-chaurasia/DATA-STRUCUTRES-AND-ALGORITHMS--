class Solution:
    
    #Function to rotate a linked list.
    def rotate(self, head, k):
        temp=head
        while temp.next:
            temp=temp.next
        temp.next=head
        p=head
        
        for i in range(k):
            ptr=p
            p=p.next
        ptr.next=None
        
        return p
