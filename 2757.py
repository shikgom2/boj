import sys
input = sys.stdin.readline

def to_base26(num):
    if num == 0:
        return "A"
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    while num > 0:
        num -= 1
        result = alphabet[num % 26] + result
        num //= 26
    return result

while(True):
    s = input().rstrip()
    if(s == 'R0C0'):
        break
    
    idxc = int(s.index('C'))

    r = s[1: idxc]
    c = s[idxc+1 : ]

    ans = to_base26(int(c))
    print(ans, end="")
    print(r)