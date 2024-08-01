n = int(input())
seven = 0
for _ in range(3):
    li = list(map(int, input().split()))
    if 7 in li:
        seven += 1
if seven == 3:
    print(777)
else:
    print(0)