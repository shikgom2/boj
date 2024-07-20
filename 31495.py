li = input()

if li[0] == li[-1] == '"' and len(li[1:-1]) > 0:
    print(li[1:-1])
else:
    print("CE")