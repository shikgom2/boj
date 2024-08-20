import sys
input = sys.stdin.readline
n=int(input())

ans1, ans2, ans3, ans4, axis = 0,0,0,0,0
for _ in range(n):
    x,y =map(int, input().split())
    
    if(x == 0 or y == 0):
        axis += 1
    elif(x > 0 and y > 0):
        ans1 += 1
    elif(x < 0 and y > 0):
        ans2 += 1
    elif(x < 0 and y < 0):
        ans3 += 1
    elif(x > 0 and y < 0):
        ans4 += 1

print(f"Q1: {ans1}")
print(f"Q2: {ans2}")
print(f"Q3: {ans3}")
print(f"Q4: {ans4}")
print(f"AXIS: {axis}")