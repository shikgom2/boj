import sys
input = sys.stdin.readline 

n,m = map(int, input().split())
st = []
li = list(map(int, input().rstrip()))

cur = 0
for i in range(n):
    st.append(li[i])
    cur += 1
    
    while(True):
        if(st[cur - 2] < st[cur - 1] and m > 0):
            del st[cur-2]
            m -= 1
            cur -= 1
        else:
            break

if(m > 0):
    for i in range(m):
        del st[-1]

print(*st, sep="")