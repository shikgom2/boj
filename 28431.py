d = {}
for i in range(10):
    d[i] = 0

for _ in range(5):
    i = int(input())
    d[i] += 1

for k, v in d.items():
    if(v % 2 == 1):
        print(k)