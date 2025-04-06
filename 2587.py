import sys
input = sys.stdin.readline

li = [int(input().strip()) for _ in range(5)]
li.sort()
print(sum(li) // 5)
print(li[2])