import sys
input = sys.stdin.readline

'''
g(0) = 0
g(1) = 0 
g(2) = 1
g(3) = mex(g(0) ^ g(1))
g(4) = mex(g(0) ^ g(2),  g(1) ^ g(3))
...
'''
def find_mex(arr):
    num_set = set(arr)
    mex = 0
    while mex in num_set:
        mex += 1
    return mex

dp = [0] * 5001
dp[0] = 0
dp[1] = 0
dp[2] = 1

for i in range(3, 5001):
    li = []
    for j in range(i-1):
        li.append((dp[j] ^ dp[i-2-j]))

    dp[i] = find_mex(li)

t = int(input())

for _ in range(t):
    n = int(input())
    if(dp[n]):
        print("First")
    else:
        print("Second")