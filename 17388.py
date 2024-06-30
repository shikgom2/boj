li = list(map(int, input().split()))
name = ['Soongsil', 'Korea', 'Hanyang']
if(sum(li) >= 100):
    print("OK")
else:
    print(name[li.index(min(li))])