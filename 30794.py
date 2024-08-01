lv, judge = input().split()
lv = int(lv)
if judge == "miss":
    print(0)
elif judge == "bad":
    print(200 * lv)
elif judge == "cool":
    print(400 * lv)
elif judge == "great":
    print(600 * lv)
else:
    print(1000 * lv)