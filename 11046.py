import sys
input = sys.stdin.readline

def solve(s):
    A = '@#' + '#'.join(s) + '#$'
    for i in range(1, len(s) // 2 + 1):
        if s[i-1] != s[-i]:
            return 0
    return 1

s = input()
arr = list(map(str, input().split()))
N = int(input())

result = []
while(True):
    N -= 1
    i,j = map(int, input().split())
    
    tmp = arr[i-1:j]

    result.append(solve(tmp))

    if(N == 0):
        break

for res in result:
    print(res)