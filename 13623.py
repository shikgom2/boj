import sys
input = sys.stdin.readline
li = list(map(int, input().split()))

if sum(li) == 0 or sum(li) == 3:
    print("*")
if sum(li) == 1:
    for i in range(len(li)):
        if li[i] == 1:
            if i == 0:
                print("A")
            elif i == 1:
                print("B")
            else:
                print("C")
if sum(li) == 2:
    for i in range(len(li)):
        if li[i] == 0:
            if i == 0:
                print("A")
            elif i == 1:
                print("B")
            else:
                print("C")