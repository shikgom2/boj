import calendar
day = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
n, m =map(int,input().split())
k = calendar.weekday(2007,n ,m)

print(day[k])