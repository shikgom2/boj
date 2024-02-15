a,b = map(int, input().split())
array = list(map(int, input().split()))
n = len(array)
prefix_sum = [0] * (n + 1)

for i in range(n):
    prefix_sum[i + 1] = prefix_sum[i] + array[i]
        
for i in range(b):
    n,m = map(int, input().split())
    print(prefix_sum[m] - prefix_sum[n - 1])