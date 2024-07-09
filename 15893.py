MAXN = 100100
SIGMA = 26
BASE = ord('a')

s = [''] * MAXN

class State:
    def __init__(self):
        self.len = 0
        self.link = 0
        self.to = [0] * SIGMA

st = [State() for _ in range(MAXN + 2)]

class Eertree:
    def __init__(self):
        self.last = 1
        self.sz = 2
        self.n = 0
        st[0].len = st[0].link = -1
        st[1].len = st[1].link = 0

    def extend(self):
        c = s[self.n]
        self.n += 1
        p = self.last

        while self.n - st[p].len - 2 < 0 or c != s[self.n - st[p].len - 2]:
            p = st[p].link

        if not st[p].to[ord(c) - BASE]:
            q = self.last = self.sz
            self.sz += 1
            st[p].to[ord(c) - BASE] = q
            st[q].len = st[p].len + 2

            while True:
                p = st[p].link
                if p == -1 or (self.n >= st[p].len + 2 and 
                               c == s[self.n - st[p].len - 2]):
                    break

            if p == -1:
                st[q].link = 1
            else:
                st[q].link = st[p].to[ord(c) - BASE]
            return 1

        self.last = st[p].to[ord(c) - BASE]
        return 0