s = input().upper()
li = list(set(s))
lst = []

for i in li:
    count = s.count(i)
    lst.append(count)

if lst.count(max(lst))>= 2:
    print("?")
else:
    print(li[lst.index(max(lst))])