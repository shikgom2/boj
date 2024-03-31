n,k = map(int, input().split())
li = list(map(int, input().split()))

ans = []

cnt = 0
for i in range(k):
    if li[i] not in ans:
        if len(ans) == n:
            if i == k - 1:
                cnt += 1
                break
            else:
                for j in ans:
                    if j not in li[i + 1:]:
                        ans.remove(j)
                        break
                else:
                    t = [li[i + 1:].index(j) for j in ans]
                    ans.pop(t.index(max(t)))
                cnt += 1
                ans.append(li[i])
        else:
            ans.append(li[i])
print(cnt)
