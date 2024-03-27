n=int(input())

for i in range(n):
    li = list(map(int, input().split()))
    li.sort()

    print(f"Scenario #{i+1}:")
    if(li[2] * li[2] == li[0] * li[0] + li[1] * li[1]):
        print("yes")
    else:
        print("no")
    if(i<n):
        print()