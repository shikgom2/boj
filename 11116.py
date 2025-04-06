import sys
input = sys.stdin.readline 

t = int(input().strip())
for _ in range(t):
    m = int(input().strip())
    left = list(map(int, input().split()))
    right = list(map(int, input().split()))
    
    ans = 0
    left.sort()
    right.sort()
    while left or right:
        if left and right:
            if left[0] < right[0]:
                direction = "left"
                t_val = left[0]
            else:
                direction = "right"
                t_val = right[0]
        elif left:
            direction = "left"
            t_val = left[0]
        else:
            direction = "right"
            t_val = right[0]

        if direction == "left":
            left.remove(t_val)
            left.remove(t_val + 500)
            right.remove(t_val + 1000)
            right.remove(t_val + 1500)
            ans += 1
        else:
            right.remove(t_val)
            right.remove(t_val + 500)
            left.remove(t_val + 1000)
            left.remove(t_val + 1500)

    print(ans)
