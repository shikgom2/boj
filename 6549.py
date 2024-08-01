import sys
input = sys.stdin.readline

while(True):
    li = list(map(int, input().split()))
    if(li[0] == 0):
        break

    n = li[0]
    del li[0]
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