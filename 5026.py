n = int(input())
for _ in range(n):
    s = input()
    print('skipped' if s=='P=NP' else eval(s))