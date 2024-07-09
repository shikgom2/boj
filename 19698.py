n,w,h,l = map(int, input().split())
ans = min((w//l) * (h//l) , n)
print(ans)