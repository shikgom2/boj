mem = [5,8]

i = int(input())
i = i - 5

for j in range(0, i):
    mem.append(mem[j] + mem[j+1])

mod = 1000000007
print (f'{mem[i] % mod} {(i+3) % mod}')
