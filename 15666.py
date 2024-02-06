N, M = map(int, input().split())
numbers = [int(x) for x in input().split()]
numbers.sort()
ans = []

memo = set()
def back(start):
    if len(ans) == M:
        tuple_ans = tuple(ans)
        if tuple_ans not in memo:
            print(" ".join(map(str, ans)))
            memo.add(tuple_ans)
        return

    for i in range(start, N+1):
        ans.append(numbers[i-1])
        back(i)
        ans.pop()

back(1)
