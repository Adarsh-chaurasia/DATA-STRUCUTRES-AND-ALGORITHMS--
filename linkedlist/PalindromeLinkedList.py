class Solution:
    def isPalindrome(self, head):
        temp=head
        stack=[]
        while temp!=None:
            stack.append(temp.data)
            temp=temp.next
        flag=True
        while head!=None:
            x=stack.pop()
            if head.data!=x:
                flag=False
                break
            head=head.next
        if flag:
            return 1
        else:
            return 0
