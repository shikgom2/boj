N, M = map(int, input().split())
numbers = [int(x) for x in input().split()]
numbers.sort()
ans = []
visited = [False] * N

def back():
    if len(ans) == M:
        print(" ".join(map(str, ans)))
        return
    flag = 0

    for i in range(N):
        if not visited[i] and flag != numbers[i]:
            visited[i] = True
            ans.append(numbers[i])
            flag = numbers[i]
            back()
            visited[i] = False
            flag = numbers[i]
            ans.pop()
back()