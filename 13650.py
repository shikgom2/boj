N, M = map(int, input().split())
ans = []

def back(start):
    # 출력
    if len(ans) == M:
        print(" ".join(map(str, ans)))
        return

    for i in range(start, N+1):
        if i not in ans:
            ans.append(i)
            back(i+1)
            ans.pop()
back(1)