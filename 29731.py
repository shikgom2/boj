i = int(input())
flag = False
for _ in range(i):
    eq = input()

    if(eq == "Never gonna give you up" or 
       eq == "Never gonna let you down" or 
       eq == "Never gonna run around and desert you" or 
       eq == "Never gonna make you cry" or 
       eq == "Never gonna say goodbye" or 
       eq == "Never gonna tell a lie and hurt you" or
        eq == "Never gonna stop"):
        flag = True

if(flag):
    print("Yes")
else:
    print("No")