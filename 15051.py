import sys
input = sys.stdin.readline

num1 = int(input().rstrip())
num2 =int(input().rstrip())
num3 = int(input().rstrip())
print(min([num1 * 2 + num2, num1 + num3, num3 * 2 + num2]) * 2)