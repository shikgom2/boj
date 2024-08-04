import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    li = list(map(int, input().split()))
    dic = {}
    for i in range(10):
        dic[i] = []

    for i in range(n):
        dic[li[i]].append(i)
    
    print(dic)