n, m = map(int,input().rsplit())
nums = list(map(int,input().rsplit()))

l, r = 0, 0
answer, hap = 0, 0

for l in range(n):
    while hap < m and r < n:
        hap += nums[r]
        r += 1
    if hap == m:
        answer += 1
    hap -= nums[l]

print(answer)