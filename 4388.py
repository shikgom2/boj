while True:
    a, b = input().split()
    if a == '0' and b == '0':
        break
    
    carry = 0
    count = 0
    a_rev = a[::-1]
    b_rev = b[::-1]
    mx = max(len(a_rev), len(b_rev))
    
    for i in range(mx):
        digit_a = int(a_rev[i]) if i < len(a_rev) else 0
        digit_b = int(b_rev[i]) if i < len(b_rev) else 0
        total = digit_a + digit_b + carry
        if total >= 10:
            count += 1
            carry = 1
        else:
            carry = 0
    print(count)
