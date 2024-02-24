str_ = input()
arr = []
for i in range(len(str_)):
    arr.append(str_[i:])
arr = sorted(arr)
print("\n".join(arr))