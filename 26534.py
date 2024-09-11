import sys
input = sys.stdin.readline

li1 = list(map(int, input().split()))
li2 = list(map(int, input().split()))

win = 0
lose = 0
match = 0
for i in range(len(li1)):
    for j in range(len(li2)):
        if(li1[i] > li2[j]):
            win += 1
            match += 1
        elif(li1[i] < li2[j]):
            lose += 1
            match += 1

ans = win / match 
print(f"{ans:.5f}")