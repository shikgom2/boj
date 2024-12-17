a, b, c = map(int, input().split())
nums = [a,b,c]
nums.sort()

s1, s2, s3 = nums[0], nums[1], nums[2]

if (s3 + s1) == 2*s2:
    x = 2*s1 - s2
    print(x)
    exit()


if (s1 + s2) % 2 == 0:
    x = (s1 + s2) // 2
    if (s2 - x) == (x - s1) and (s3 - s2) == (s2 - x):
        print(x)
        exit()

x = 2*s2 - s1
if (x > s2) and ((s2 - s1) == (x - s2) == (s3 - x)):
    print(x)
    exit()

if (s3 + s1) == 2*s2:
    x = 2*s3 - s2
    print(x)
    exit()
