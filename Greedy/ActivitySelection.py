class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        result=[]
        for i in range(len(start)):
            result.append((start[i],end[i]))
            
        result.sort(key=lambda x:x[1])
        i=0
        ans=[]
        ans.append(result[i])
        j=1
        while j<len(result):
            if result[i][1]<result[j][0]:
                ans.append(result[j])
                i=j
                j+=1
                
            else:
                j+=1
                
                
        return len(ans)
