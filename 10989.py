import sys
input = sys.stdin.readline
i = int(input())
lists = [0] * 10001

for i in range(i):
    k = int(input())
    lists[k] += 1

for i in range(1, 10001):
    if(lists[i] > 0):
        while(True):
            print(i)
            lists[i] -= 1

            if(lists[i] == 0):
                break