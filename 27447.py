import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = list(map(int, input().split()))

togi = 0 # togi 갯수
time = 0 # 현재 시간

#timeline에 오는 손님 저장
timeline = [0] * 1000001
for i in li:
    timeline[i] = 1

#각 손님별로 쿼리
for t in li:
    #1. (현재 시간 ~ 손님 오는 시간 - m) 까지 togi 제작
    while(time < t - m):
        if timeline[time] == 0:
            togi += 1
        time += 1

    #2-1. togi 있으면 담고 내놓기
    if(togi > 0):
        while(time < t):
            if(timeline[time] == 0):
                break
            else:
                time += 1
        if(time < t):
            time += 1
            togi -= 1
        else:
            print('fail')
            exit()
    #2-2. togi 없으면 togi 만들고 담고 내놓기
    else:
        while(time < t):
            if(timeline[time] == 0):
                togi += 1
                time += 1
                break
            time += 1
        while(time < t):
            if timeline[time] == 0:
                break
            time += 1
        if(time < t):
            time += 1
            togi -= 1
        else:
            print('fail')
            exit()

print('success')