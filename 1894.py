import sys
while True:
    try:    
        x1, y1, x2, y2, x3, y3, x4, y4 = map(float, input().split())
    except EOFError:
        break    
    A = (x1, y1)
    B = (x2, y2)
    C = (x3, y3)
    D = (x4, y4)
    
    if B == C:
        dx = A[0] + D[0] - B[0]
        dy = A[1] + D[1] - B[1]
    elif A == C:
        dx = B[0] + D[0] - A[0]
        dy = B[1] + D[1] - A[1]
    elif A == D:
        dx = B[0] + C[0] - A[0]
        dy = B[1] + C[1] - A[1]
    elif B == D:
        dx = A[0] + C[0] - B[0]
        dy = A[1] + C[1] - B[1]
    else:
        dx, dy = 0.0, 0.0
    print("{0:.3f} {1:.3f}".format(dx, dy))