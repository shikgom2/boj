
while True:
    s = input()
    if s== 'EOI': 
        exit()

    print('Found' if 'nemo' in s.lower() else 'Missing')