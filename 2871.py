n = int(input())
li = list(map(str, input().strip()))

li.sort()
s1 = ""
s2 = ""

# 100000개니까 완전탐색해도 ㄱㅊ을거같음.
# 젤 오른쪽에서 a 찾고 b찾고...순으로 그리디하게
# 젤오른쪽 제거