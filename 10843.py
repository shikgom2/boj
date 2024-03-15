def checklen(q):
    if(len(q) == 0):
        print(-1)
        return True
    return False

N = int(input())

q = []
for _ in range(N):
    s = list(map(str, input().split()))

    if(s[0] == 'push'):
        q.append(s[1])
    