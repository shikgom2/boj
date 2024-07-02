t = int(input())
for i in range(t):
    n = int(input())
    k = " "
    if(n > 4500):
        k = "Round 1"
    elif(n > 1000):
        k = "Round 2"
    elif(n > 25):
        k = "Round 3"
    else:
        k = "World Finals"

    print(f"Case #{i+1}: {k}")