import sys
input = sys.stdin.readline

def failure(pattern):
    fail = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = fail[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            fail[i] = j
    return fail

n = int(input())

patterns = []
for _ in range(n):
    a = input().rstrip().split()
    patterns.append(a[1])

a = input().rstrip().split()
target = a[1]

# Collect all occurrences of patterns in target
positions = []
for idx, pattern in enumerate(patterns):
    fail = failure(pattern)
    j = 0
    for i, char in enumerate(target):
        while j > 0 and char != pattern[j]:
            j = fail[j - 1]
        if char == pattern[j]:
            j += 1
            if j == len(pattern):
                start_pos = i - len(pattern) + 1
                end_pos = i
                positions.append((start_pos, end_pos, idx))
                j = fail[j - 1]

# Sort the occurrences by start position
positions.sort(key=lambda x: x[0])

from collections import defaultdict

left = 0
ans = len(target)
counts = defaultdict(int)
total_patterns = 0
required_patterns = n

# Sliding window over the sorted positions
for right in range(len(positions)):
    start_r, end_r, idx_r = positions[right]
    if counts[idx_r] == 0:
        total_patterns += 1
    counts[idx_r] += 1

    # Try to shrink the window from the left
    while total_patterns == required_patterns and left <= right:
        start_l, end_l, idx_l = positions[left]
        current_length = max(end_r, positions[right][1]) - start_l + 1
        ans = min(ans, current_length)
        counts[idx_l] -= 1
        if counts[idx_l] == 0:
            total_patterns -= 1
        left += 1

print(ans)
