import bisect

def lis(li):
    lis = []
    idx_list = []
    trace = [-1] * len(li)
    
    for i in range(len(li)):
        pos = bisect.bisect_left(lis, li[i])
        if pos < len(lis):
            lis[pos] = li[i]
        else:
            lis.append(li[i])
        idx_list.append((pos, li[i]))

    # LIS 구성에 필요한 인덱스 추적
    lis_len = len(lis)
    lis_elements = []
    current_pos = lis_len - 1
    
    for i in range(len(idx_list) - 1, -1, -1):
        if idx_list[i][0] == current_pos:
            lis_elements.append(idx_list[i][1])
            current_pos -= 1
    
    return lis_elements[::-1]

n = int(input())
li = []
dic = {}
for _ in range(n):
    a, b = map(int, input().split())
    li.append((a, b))
    dic[b] = a

li.sort()
check = [li[i][1] for i in range(n)]

# LIS 계산
ans = lis(check)

# LIS에 포함되지 않은 b값 찾기
lis_set = set(ans)
remove_list = [b for b in check if b not in lis_set]

# 정답 출력
print(len(remove_list))
remove_a_values = sorted(dic[b] for b in remove_list)
for a in remove_a_values:
    print(a)
