import sys
input = sys.stdin.readline

while True:
    try:
        line = input()
    except:
        break
    
    print(bytes.fromhex(line).decode('utf-8'))