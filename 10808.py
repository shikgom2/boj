i = list(input().strip())
li = {chr(i): 0 for i in range(ord('a'), ord('z')+1)}
for s in i:
    li[s] += 1
sorted(li)
for k in li.values():
    print(k, end=" ")