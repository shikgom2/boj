import sys
input = sys.stdin.readline


a_b, a_a = map(int, input().split())
b_b, b_a = map(int, input().split())
c_b, c_a = map(int, input().split())
d_b, d_a = map(int, input().split())

ans3 = d_a - d_b
ans2 = (c_a - c_b) + ans3
ans1 = (b_a - b_b) + ans2

print(ans1)
print(ans2)
print(ans3)