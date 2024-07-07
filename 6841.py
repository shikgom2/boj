li = ["CU", ":-)", ":-(", ";-)", ":-P", "(~.~)", "TA", "CCC", "CUZ", "TY", "YW", "TTYL"]
ans = ["see you", "I’m happy", "I’m unhappy", "wink", "stick out my tongue", "sleepy", "totally awesome", "Canadian Computing Competition", "because", "thank-you", "you’re welcome", "talk to you later"]
while True:
    s = input()
    if(s in li):
        print(ans[li.index(s)])
    else:
        print(s)
    if (s == "TTYL"):
        break