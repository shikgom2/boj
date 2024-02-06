#Input
string = str(input())
length = len(string)
#Initlaize
A = [0] * (length + 2)
B = [0] * (length + 2)

A[length + 1] = 1
B[length + 1] = 0

for i in range(length, 0, -1):
    if string[i - 1] == 'P':
        A[i] = A[i + 1]
        B[i] = B[i + 1]
    elif string[i - 1] == 'L':
        A[i] = 2 * A[i + 1]
        B[i] = B[i + 1]
    elif string[i - 1] == 'R':
        A[i] = 2 * A[i + 1]
        B[i] = A[i + 1] + B[i + 1]
    elif string[i - 1] == '*':
        A[i] = 5 * A[i + 1]
        B[i] = A[i + 1] + 3 * B[i + 1]

print(A[1] + B[1])