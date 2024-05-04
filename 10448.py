
li = []
ans = [0] * 1001
for i in range(1, 100):
    li.append(i * (i + 1) // 2)

for i in li:
    for j in li:
        for k in li:
            if(i+j+k <= 1000):
                ans[i+j+k] = 1

n = int(input())
for _ in range(n):
    a = int(input())
    print(ans[a])