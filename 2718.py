dp_a = [0,1,5] * 100
dp_b = [0,1,2] * 100
dp_c = [0,0,1] * 100

for i in range(3, 27):
    dp_c[i] = dp_a[i-2] + dp_c[i-2]
    dp_b[i] = dp_b[i-1] + dp_a[i-1]
    dp_a[i] = dp_b[i] + dp_c[i-2] + dp_a[i-2] + dp_a[i-2] + dp_b[i-1]

T = int(input())
for _ in range(T):
    N = int(input())
    print(dp_a[N])
