N = int(input())
for _ in range(N):
    i,j = map(str, input().split())

    s = 0
    for k in j:
        s += int(k)
    print(s % (int(i)-1))