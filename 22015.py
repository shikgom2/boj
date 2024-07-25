stars = list(map(int, input().split()))

print(max(stars) * 3 - sum(stars))