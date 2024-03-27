n = int(input())
li = list(map(int, input().split()))
k = int(input())

if(k == li[0]):
    print("T")
    exit()

for i in range(1, n):
    if(1 * k * i <= li[i-1] and li[i] <= 1 * k * (i+1)):
        print("T")
        exit()

print("F")
