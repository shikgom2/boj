li = [
    " @@@   @@@ ",
    "@   @ @   @",
    "@    @    @",
    "@         @",
    " @       @ ",
    "  @     @  ",
    "   @   @   ",
    "    @ @    ",
    "     @     ",
]
n = int(input())
for l in li:
    k = [l for _ in range(n)]
    print(" ".join(k))