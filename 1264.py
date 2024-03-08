import sys
from collections import defaultdict

checkList = ["A", "E", "O", "U", "I", "a", "e", "o", "u", "i"]
T = input()
while T != "#":
    d = defaultdict(int)
    for i in T:
        if i in checkList:
            d[i] += 1
    s = [i for i in d.values()]
    print(sum(s))
    T = input()