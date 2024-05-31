
li = {"e": "i", "i": "e", "E": "I", "I": "E"}

while True:
    try:
        s = input()
    except EOFError:
        break

    ans = [li[word] if word in li else word for word in list(s)]
    print("".join(ans))