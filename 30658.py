while True:
    n = int(input())
    if n == 0:
        break

    li = []
    for _ in range(n):
        li.append(int(input()))

    while li:
        print(li.pop())
    print(0)