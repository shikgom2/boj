for _ in range(3):
    T = int(input())
    li = []
    for i in range(T):
        li.append(int(input()))
    res = sum(li)
    if res > 0:
        print("+")
    elif res == 0:
        print(0)
    else:
        print("-")