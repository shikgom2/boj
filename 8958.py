N=int(input())
for _ in range(N):
    a = input()
    c=1
    s=0
    for j in a:
        if j == 'O':
            s += c
            c += 1
        else:
            c = 1
    print(s)