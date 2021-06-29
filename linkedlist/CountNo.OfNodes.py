class Solution:
    
    #Function to count nodes of a linked list.
    def getCount(self, head):
        temp=head
        count=0
        while temp:
            count+=1
            temp=temp.next
            
            
        return count
      
      
      
      
#recursive


class Solution:
    
    #Function to count nodes of a linked list.
    def getCount(self, head):
        if not head:
            return 0
            
        else:
            return 1+self.getCount(head.next)
