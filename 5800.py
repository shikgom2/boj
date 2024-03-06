import sys
input = sys.stdin.readline

n = int(input().strip())
for i in range(n):
    num = list(map(int, input().split()))
    k = num[0]
    num = num[1:]
    num.sort()
    print(f'Class {i+1}')
    li = []
    for j in range(k-1):
        li.append(num[j+1]-num[j])
    li.sort()

    print(f'Max {num[-1]}, Min {num[0]}, Largest gap {li[-1]}')