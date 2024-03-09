from sys import stdin
s = ""
for n in stdin.readlines():
    s += n.replace('\n', '')
print(sum(map(int, s.split(','))))