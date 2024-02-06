from itertools import combinations

# 입력 받기
numbers = sorted(set(map(int, input().split())))

# 가능한 조합 출력
for combination in combinations(numbers, 2):
    print(" ".join(map(str, combination)))