import sys
input = sys.stdin.readline
from collections import deque
li = list(map(str, input().rstrip()))

st = deque()
for i in range(len(li)):
    if(li[i].isdigit()):
        st.append(li[i])
    else:
        if(li[i] == '+'):
            ans = int(st[-1]) + int(st[-2])
            st.pop()
            st.pop()
            st.append(ans)
        elif(li[i] == '-'):
            ans = int(st[-2]) - int(st[-1])
            st.pop()
            st.pop()
            st.append(ans)
        elif(li[i] == '*'):
            ans = int(st[-1]) * int(st[-2])
            st.pop()
            st.pop()
            st.append(ans)
        elif(li[i] == '/'):
            ans = int(st[-2]) // int(st[-1])
            st.pop()
            st.pop()
            st.append(ans)

print(st[0])