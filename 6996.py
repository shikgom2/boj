import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    a, b = map(str, input().split())

    print(f'{a} & {b} are ',end='')

    a = str.join('',sorted(a))
    b = str.join('',sorted(b))

    if a == b: print('anagrams.')
    else: print('NOT anagrams.')