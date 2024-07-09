n,m,k = map(int, input().split())

f_1 = m
f_2 = (n-m)

b_1 = k
b_2 = (n - k)

print(min(f_1, b_1) + min(f_2, b_2))