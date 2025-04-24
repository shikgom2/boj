import sys
input = sys.stdin.readline

while True:
    H1, M1, H2, M2 = map(int, input().split())
    # 종료 조건
    if H1 == 0 and M1 == 0 and H2 == 0 and M2 == 0:
        break

    start = H1 * 60 + M1       # 현재 시각을 분 단위로
    alarm = H2 * 60 + M2       # 알람 시각을 분 단위로

    # 알람이 같은 날 이후라면 하루(1440분) 더해 줌
    if alarm <= start:
        alarm += 24 * 60

    print(alarm - start)
