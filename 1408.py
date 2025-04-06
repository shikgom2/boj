import sys
input = sys.stdin.readline

cur = input().strip()
st = input().strip()

ch, cm, cs = map(int, cur.split(':'))
sh, sm, ss = map(int, st.split(':'))
cur_sec = ch * 3600 + cm * 60 + cs
st_sec = sh * 3600 + sm * 60 + ss

if cur_sec < st_sec:
    remain = st_sec - cur_sec
else:
    remain = 24 * 3600 - (cur_sec - st_sec)

h = remain // 3600
m = (remain % 3600) // 60
s = remain % 60

print(f"{h:02d}:{m:02d}:{s:02d}")

