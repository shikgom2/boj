import sys
input = sys.stdin.readline
n= int(input())
li = list(map(int, input().split()))
print(n-len(set(li)))