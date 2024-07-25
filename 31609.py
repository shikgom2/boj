n = int(input())
li = list(set(map(int, input().split())))
li.sort()

for i in li:
    print(i)