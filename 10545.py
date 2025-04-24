import sys
input = sys.stdin.readline

li = list(map(int, input().split()))  # 길이 9

# 2) 원래 키별 문자 그룹 정의
dic = {
    2: "abc", 3: "def", 4: "ghi", 5: "jkl",
    6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"
}

# 3) 문자 → (물리키, 반복횟수) 매핑 생성
m = {}
for k, v in enumerate(li, start=1):
    idx = dic.get(v, "")
    for idx, ch in enumerate(idx):
        m[ch] = (k, idx + 1)

s = input().strip()

last = -1
ans = []
for ch in s:
    phys, cnt = m[ch]
    if phys == last:
        ans.append('#')
    ans.append(str(phys) * cnt)
    last = phys

print("".join(ans))