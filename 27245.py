w = int(input())
s = int(input())
h = int(input())
if min(w, s) >= h * 2 and min(w, s) * 2 >= max(w, s):
    print("good")
else:
    print("bad")