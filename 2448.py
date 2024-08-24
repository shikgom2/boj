import sys
input = sys.stdin.readline

def draw(l):
    if l == 3:
        return ['  *  ',' * * ','*****']

    li = draw(l//2)
    ans = []
    for i in li:
        ans.append(' '*(l//2)+i+' '*(l//2))

    for i in li:
        ans.append(i + ' ' + i)
        
    return ans

n = int(input())
print('\n'.join(draw(n)))