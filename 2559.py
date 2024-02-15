a,b = map(int, input().split())
array = list(map(int, input().split()))
n = len(array)
prefix_sum = [0] * (n + 1)
sum_list = []
sum_ = 0

for i in range(0, n):
    sum_ = sum_ + array[i]
    if(i == b-1):
        sum_list.append(sum_)
    if(i >= b):
        sum_ -= array[i-b]
        sum_list.append(sum_)
print(max(sum_list))