li = list(map(int, input().split()))
tmp = li[4]
del li[4]
if sum(li) >= tmp * 4:
    print(0)
else:
    print(tmp * 4 - sum(li))