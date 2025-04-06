import sys
input = sys.stdin.readline
from collections import Counter

t = int(input())
for _ in range(t):
    s = input()
    cnt = Counter(s)
    w = int(input())
    for _ in range(w):
        word = input()
        word_cnt = Counter(word)
        flag = True
        for l, v in word_cnt.items():
            if cnt[l] < v:
                flag = False
                break
        if flag:
            print("YES")
        else:
            print("NO")