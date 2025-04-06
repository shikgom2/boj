import sys
input = sys.stdin.readline

v = int(input().strip())
li = input().strip()
cnt1 = li.count("A")
cnt2 = li.count("B")

if cnt1 > cnt2:
    print("A")
elif cnt2 > cnt1:
    print("B")
else:
    print("Tie")