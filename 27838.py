import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    _ = input()
    n = int(input())
    li = list(map(int, input().split()))

    prefix_sum = 0
    dic = {0: 1}
    ans = 0

    for i in range(n):
        prefix_sum += li[i]
        diff = prefix_sum - 47
        
        if diff in dic:
            ans += dic[diff]
        
        if prefix_sum in dic:
            dic[prefix_sum] += 1
        else:
            dic[prefix_sum] = 1

    print(ans)