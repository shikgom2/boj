n,u,l = map(int, input().split())

flag = False

if(n < 1000):
    print("Bad")
elif(u >= 8000 or l >= 260):
    print("Very Good")
else:
    print("Good")