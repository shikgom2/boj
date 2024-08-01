w, h = map(int, input().split())
n, a, b = map(int, input().split())
if a > w or b > h:
    print(-1)
else:
    div, left = divmod(n, ((w // a) * (h // b)))
    if left:
        print(div + 1)
    else:
        print(div)