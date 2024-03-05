s = list(str(input()))
for c in s:
    if c in 'abcdefghijklmnopqrstuvwxyz':
        print(c.upper(), end = "")
    else:
        print(c.lower(), end = "")