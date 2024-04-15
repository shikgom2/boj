import sys
input = sys.stdin.readline

def find(black_holes, asteroid_position):
    left, right = 0, len(black_holes) - 1
    nearest_distance = float('inf')
    while left <= right:
        mid = (left + right) // 2
        distance = abs(black_holes[mid] - asteroid_position)
        nearest_distance = min(nearest_distance, distance)
        
        if black_holes[mid] < asteroid_position:
            left = mid + 1
        else:
            right = mid - 1

    return nearest_distance

def solve(black_holes, asteroids):
    black_holes.sort()
    max_P = 0
    for a_j, w_j in asteroids:
        nearest_distance = find(black_holes, a_j)
        required_P = nearest_distance * w_j
        max_P = max(max_P, required_P)
    return max_P

N, M = map(int, input().strip().split())

black_holes = list(map(int, input().strip().split()))
asteroids = [tuple(map(int, input().strip().split())) for _ in range(M)]

result = solve(black_holes, asteroids)
print(result)