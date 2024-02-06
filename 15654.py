N, M = map(int, input().split())
numbers = [int(x) for x in input().split()]
numbers.sort()
ans = []

def back(start):
    if len(ans) == M:
        print(" ".join(map(str, ans)))
        return

    for i in range(1, N+1):
        ans.append(numbers[i-1])
        back(i)
        ans.pop()
back(1)