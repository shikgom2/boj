import sys
input = sys.stdin.readline


s = input().rstrip()

if(s == '1)('):
    print(1)
elif(s == ')1('):
    print(2)
elif(s == '(1)'):
    print(0)
elif(s == ')(1'):
    print(1)
elif(s == '1()'):
    print(1)
elif(s == '()1'):
    print(1)