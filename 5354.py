n = int(input())

for i in range(n):
    a = int(input())
    if a == 1:
        print('#')
    elif a == 2:
        print('##')
        print('##')
    else:
        print('#'*a)
        for j in range(a-2):
            print('#','J'*(a-2),'#',sep='')
        print('#'*a)

    if i != n-1:
        print()