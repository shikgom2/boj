n = int(input())
li = list(set(map(int, input().split())))
li.sort()

for i in range(len(li)):
    print(li[i])