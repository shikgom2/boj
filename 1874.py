import sys
input = sys.stdin.readline

n = int(input())
st = []
ans = []
flag = True
cur = 0

for _ in range(n):
    k = int(input())
    while cur < k :
        cur += 1
        ans.append("+")
        st.append(cur)
    
    if st[-1] == k :
        st.pop()
        ans.append("-")
    else: 
        flag = False
        break

if flag:
    for i in range(len(ans)):
        print(ans[i])
else:
    print("NO")