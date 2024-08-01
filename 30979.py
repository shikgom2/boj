t = int(input())
n = int(input())
li = list(map(int, input().split()))

if t <= sum(li):
    print("Padaeng_i Happy")
else:
    print("Padaeng_i Cry")