def mex(s):
    """Compute the minimum excludant of a set."""
    i = 0
    while i in s:
        i += 1
    return i

def compute_grundy(n, removal_options):
    """Compute the Grundy number for a given number of stones."""
    if n == 0:
        return 0
    grundy = [0] * (n + 1)
    for i in range(1, n + 1):
        reachable_states = set()
        for option in removal_options:
            if i - option >= 0:
                reachable_states.add(grundy[i - option])
        grundy[i] = mex(reachable_states)
    return grundy[n]

def xor_grundy_numbers(scenarios, removal_options):
    """Compute the XOR of the Grundy numbers for multiple scenarios."""
    grundy_numbers = [compute_grundy(n, removal_options) for n in scenarios]
    result = 0
    for grundy_number in grundy_numbers:
        result ^= grundy_number
    return result, grundy_numbers



n,m = map(int, input().split())
grundy = []
for _ in range(n):
    li = list(map(str, input().strip()))
    
    cnt = 0
    for i in range(len(li)):
        #print(i)
        if(li[i] == '@' and cnt >= 1):
            grundy.append(cnt)
            cnt = 0
        else:   
            cnt += 1
            if(i == len(li)-1):
                grundy.append(cnt)
                cnt = 0
    
i = int(input())
li = list(map(int, input().split()))

#print(grundy)
ans, grundy_numbers = xor_grundy_numbers(grundy, li)
#print(ans,grundy_numbers)

if(ans != 0):
    print("nein")
else:
    print("hyo123bin")