def loop(head):
    slow=head
    fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            return slow
            
    return None

#User function Template for python3

'''
Structure of node

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

'''

#Function to find the length of a loop in the linked list.
def countNodesinLoop(head):
    p=loop(head)
    q=loop(head)
    if p==None:
        return 0
        
    count=0
    
    while 1:
        q=q.next
        count+=1
        if p==q:
            break
        
        
    return count
