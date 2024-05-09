def find_divisors(n):
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return divisors

while(True):
    n = int(input())
    if(n == -1):
        break

    li = find_divisors(n)
    li.sort()
    if(sum(li) != n):
        print(f"{n} is NOT perfect.")
    else:
        print(f"{n} = ", end="")
        for i in range(len(li)):
            if(i != len(li)-1):
                print(f"{li[i]} + ", end="")
            else:
                print(f"{li[i]}")