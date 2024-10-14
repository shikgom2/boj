import sys
input = sys.stdin.readline

li = list(map(str, input().rstrip()))
st = []
ans = []

flag = False

for a in range(len(li)):
     
    st.append(li[a])
        
    if(li[a] == '<'):
        for i in range(len(st)-2, -1, -1):
            ans.append(st[i])
        st = []
        st.append("<")
        flag = True
                
    elif(li[a] == '>'):
        for i in range(len(st)):
            ans.append(st[i])
            flag = False
        st = []

    elif(li[a] == ' ' and flag == False):
        for i in range(len(st)-2, -1, -1):
            ans.append(st[i])
        
        ans.append(" ") 
        st = []
      
for i in range(len(st)-1, -1, -1):
    ans.append(st[i])
        
print(*ans, sep="")