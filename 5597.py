items = [int(input()) for _ in range(28)]
lists = [0] * 31

for item in items:
    lists[item] = 1
lists[0] = 1

for idx, list in enumerate(lists):
    if(list == 0):
        print(idx)