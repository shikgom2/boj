import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
print(arr)
sum = 1
for i in range(N):
    if(sum < arr[i]):
        break
    sum += arr[i]

print(sum)