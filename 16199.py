a, b, c = map(int, input().split())
d, e, f=map(int, input().split())

if e>b or (e==b and f>=c):
    year1=d-a
else:
    year1=d-a-1

year2=d-a+1
year3=d-a

print(year1)
print(year2)
print(year3)    