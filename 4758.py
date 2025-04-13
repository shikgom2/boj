import sys
input = sys.stdin.readline

while True:
    line = input().strip()
    s, w, st = map(float, line.split())
    
    if s == 0 and w == 0 and st == 0:
        break
    
    li = []
    
    if s <= 4.5 and w >= 150 and st >= 200:
        li.append("Wide Receiver")
    
    if s <= 6.0 and w >= 300 and st >= 500:
        li.append("Lineman")
    
    if s <= 5.0 and w >= 200 and st >= 300:
        li.append("Quarterback")
    
    if li:
        print(" ".join(li))
    else:
        print("No positions")
