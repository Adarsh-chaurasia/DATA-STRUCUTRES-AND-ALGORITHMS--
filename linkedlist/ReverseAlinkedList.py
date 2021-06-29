class Solution:
    #Function to reverse a linked list.
    def reverseList(self, head):
        slow=head
        prev=None
        while slow:
            fast=slow.next
            slow.next=prev
            prev=slow
            slow=fast
            
        head=prev
        
        return head
