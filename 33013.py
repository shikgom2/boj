import sys
input = sys.stdin.readline
import math

n = int(input())
li = [tuple(map(int, input().split())) for _ in range(n)]

ans = 1
for i in range(n):
    x_i, y_i = li[i]
    x_i2, y_i2 = x_i*x_i, y_i*y_i
    duplicates = 0

    ratio_dict = {}

    for j in range(i+1, n):
        x_j, y_j = li[j]
        x_j2, y_j2 = x_j*x_j, y_j*y_j

        if x_i2 == x_j2 and y_i2 == y_j2:
            # 완전히 제곱이 같은 점 -> duplicate
            duplicates += 1
            continue

        # 한 쪽만 0 차이이면(즉 x^2만 같고 y^2은 다르거나 그 반대) 같은 타원 불가
        # 곱이 양수여도 (둘 다 양수 or 둘 다 음수) 같은 타원 불가
        dx = x_i2 - x_j2
        dy = y_i2 - y_j2
        if (dx == 0) ^ (dy == 0):  
            # (배타적 OR) -> 하나만 0인 경우
            continue
        if dx * dy > 0:
            # 부호 같으면 안 된다
            continue
        # 여기까지 통과하면 dx*dy <= 0 이고, dx와 dy가 동시에 0은 이미 위에서 duplicates 처리

        # 비율 R = dx/dy (dy != 0 일 때). 이 값은 항상 <=0 일 텐데,
        # gcd 로 기약분수 형태로 정규화
        if dy == 0:
            # dy=0이면 dx=0도 돼야 duplicates인데, 이미 걸렀으니 사실 여기 올 일 없음
            # 혹시나 처리한다면...
            # ratio를 (1, 0) or (-1, 0) 같은 식으로 둘 수도 있지만, 여기선 skip
            continue
        else:
            g = math.gcd(dx, dy)
            dx //= g
            dy //= g
            # 분모가 음수이면 부호를 위로 올려서 (dx, dy>0) 형태 등으로 통일
            # 하지만 "항상 음수"가 편하면 그렇게 맞춰도 됨
            # 일단 여기서는 (dx, dy)를 그대로 쓰되, dy<0면 (dx, dy)=( -dx, -dy ) 로 바꾸자
            if dy < 0:
                dx = -dx
                dy = -dy

            ratio_dict[(dx, dy)] = ratio_dict.get((dx, dy), 0) + 1

    # ratio_dict에서 최댓값 찾기
    best = 0
    if ratio_dict:
        best = max(ratio_dict.values())

    # 기준점(i) 포함 + duplicates(동일제곱 좌표) + best(최대 동시비율)
    # => 같은 타원 위에 들어갈 수 있는 점들의 최대 개수
    ans = max(ans, best + duplicates + 1)

print(ans)
