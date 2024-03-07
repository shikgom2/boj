n = int(input())
s = input()
sec = s.count('s')
big = s.count('b')

if(sec == big):
    print('bigdata? security!')
elif sec > big:
    print('security!')
else: 
    print('bigdata?')