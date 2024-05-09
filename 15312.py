def alphabet_to_number(c):
    return ord(c) - ord('A') + 1

s1 = input().strip()
s2 = input().strip()
li = [0, 3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

n1 = []
n2 = []
for i in s1:
    n1.append(li[alphabet_to_number(i)])
for i in s2:
    n2.append(li[alphabet_to_number(i)])
n = []
for i in range(len(n1)):
    n.append(n1[i])
    n.append(n2[i])

idx = len(n)
while(True):
    for i in range(len(n)-1):
        n.append((n[i] + n[i+1]) % 10)

    del n[0: idx]
    idx -= 1
    if(len(n) <= 2):
        break

ans = n[0] * 10 + n[1]
if(ans < 10):
    print("0",end="")
print(ans)