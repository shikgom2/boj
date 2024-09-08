import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

li.sort()
print(max(sum(li)/n, li[n-2]))