import sys
import bisect
input = sys.stdin.readline

N, M, K = map(int, input().split())

keys = []
dic = {}
for _ in range(N):
    key, value = map(int, input().split())
    keys.append(key)
    dic[key] = value
keys.sort()

def getClosest(query):
    n = len(keys)
    pos = bisect.bisect_left(keys, query)
    bestKey = -1
    bestDiff = float('inf')
    status = 0 
    
    if pos < n:
        diff = abs(keys[pos] - query)
        bestDiff = diff
        bestKey = keys[pos]
        status = 1
    
    if pos > 0:
        diff = abs(keys[pos - 1] - query)
        if diff < bestDiff:
            bestDiff = diff
            bestKey = keys[pos - 1]
            status = 1
        elif diff == bestDiff:
            status = 2
    
    if bestDiff > K:
        return (-1, 0)
    return (bestKey, status)

for _ in range(M):
    command = input().split()
    if not command:
        continue
    cmd_type = command[0]
    if cmd_type == '1':
        key = int(command[1])
        value = int(command[2])
        bisect.insort(keys, key)
        dic[key] = value
    elif cmd_type == '2':
        query = int(command[1])
        newVal = int(command[2])
        closest, status = getClosest(query)
        if closest == -1 or status == 2:
            continue
        dic[closest] = newVal
    elif cmd_type == '3':
        query = int(command[1])
        closest, status = getClosest(query)
        if closest == -1:
            print("-1")
        elif status == 2:
            print("?")
        else:
            print(str(dic[closest]))


