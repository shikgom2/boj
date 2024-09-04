import sys
input = sys.stdin.readline

n = int(input())
li = []

li.append("")
li.append("A B C D E F G H J L M")
li.append("A C E F G H I L M")
li.append("A C E F G H I L M")
li.append("A B C E F G H L M")
li.append("A C E F G H L M")
li.append("A C E F G H L M")
li.append("A C E F G H L M")
li.append("A C E F G H L M")
li.append("A C E F G H L M")
li.append("A B C F G H L M")

if(n == 1):
    print(11)
elif(n <= 4):
    print(9)
else:
    print(8)
print(li[n])