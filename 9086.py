N=int(input())
for _ in range(N):
    s = input()
    if(len(s) >= 2):
        print(f'{s[0]}{s[-1]}')
    else:
        print(f'{s[0]}{s[0]}')