import sys
input = sys.stdin.readline
sys.setrecursionlimit(155557)

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def sieve(n):
    primes = [True]*(n+1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5)+1):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False
    return primes

def dfs(u, adj, c, visited):
    for v in adj[u]:
        if not visited[v]:
            visited[v] = True
            if c[v] == -1 or dfs(c[v], adj, c, visited):
                c[v] = u
                return True
    return False

n = int(input())
arr = list(map(int, input().split()))

mx = max(arr) * 2
primes = sieve(mx)

first = arr[0]

odds = []
evens = []
for num in arr:
    if num % 2 == 0:
        evens.append(num)
    else:
        odds.append(num)

if first % 2 == 0:
    first_group = evens
    second_group = odds
else:
    first_group = odds
    second_group = evens

li = []
for num in second_group:
    if primes[first + num]:
        li.append(num)

ans = []
for a in range(len(li)):
    g1 = first_group.copy()
    g2 = second_group.copy()
    g1.remove(first)
    g2.remove(li[a])
    
    if len(g1) != len(g2):
        continue  # 남은 두 그룹의 크기가 다르면 완전 매칭 불가
    
    adj = [[] for _ in range(len(g1))]
    for i, u in enumerate(g1):
        for j, v in enumerate(g2):
            if primes[u + v]:
                adj[i].append(j)

    c = [-1]*len(g2)
    res = 0
    for i in range(len(g1)):
        visited = [False]*len(g2)
        if dfs(i, adj, c, visited):
            res += 1

    if res == len(g1):
        ans.append(li[a])

if ans:
    print(' '.join(map(str, sorted(ans))))
else:
    print(-1)
