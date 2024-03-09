def reverse(i):
    i = i[::-1]
    i = int(i)
    return i 

x, y = map(str, input().split())
print(reverse(str(reverse(x)+reverse(y))))