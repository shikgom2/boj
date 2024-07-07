li = []
for _ in range(4):
    k = int(input())
    li.append(k)

if(li[0] < li[1] and li[1] < li[2] and li[2] < li[3]):
    print("Fish Rising")
elif(li[0] > li[1] and li[1] > li[2] and li[2] > li[3]):
    print("Fish Diving")
elif(max(li) == min(li)):
    print("Fish At Constant Depth")
else:
    print("No Fish")