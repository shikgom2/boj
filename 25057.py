def check(s):
    b = 0
    li = []
    for c in s:
        if c == 'B': 
            b += 1
        elif not li or li[-1] != c: 
            li.append(c)
        else: 
            li.pop()
    if b % 2: 
        li.append('B')
    return li

t = int(input())
for _ in range(t):
    s1 = input()
    s2 = input()

    if(check(s1) == check(s2)):
        print('YES')
    else: print('NO')