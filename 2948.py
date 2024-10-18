import sys
input = sys.stdin.readline 

year = [31,28,31,30,31,30,31,31,30,31,30,31]
week = ['Thursday','Friday','Saturday','Sunday','Monday','Tuesday','Wednesday']
day, month = map(int, input().split())
day += sum(year[0:month-1])-1

print(week[day%7])