import sys
input = sys.stdin.readline

n = int(input())
li = []
for _ in range(n):
    k = int(input())
    li.append(k)

st = []
ans = 0
n = len(li)

for i in range(n + 1):
    while st and (i == n or li[st[-1]] > li[i]):
        top = st.pop()
        
        if(len(st) == 0):
            bot = i
        else:
            bot = i - st[-1] - 1

        ans = max(ans, li[top] * bot)
    st.append(i)

print(ans)