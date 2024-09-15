import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
class Parser:
    def __init__(self, s):
        self.s = s
        self.n = len(s)
        self.pos = 0
        self.depth_hashes = {}
        self.memo = {}
        self.id_counter = 2
    
    def parse(self):
        stack = []
        while self.pos < self.n:
            if self.s[self.pos] == '(':
                stack.append([])
                self.pos += 1
            elif self.s[self.pos] == ')':
                child_ids = stack.pop()
                child_depths = [depth for depth, _ in child_ids] if child_ids else []
                
                if not child_depths:
                    depth = 1
                    id_ = 1
                else:
                    depth = 1 + max(child_depths)
                    child_ids_sorted = tuple(sorted(id_ for _, id_ in child_ids))
                    if child_ids_sorted in self.memo:
                        id_ = self.memo[child_ids_sorted]
                    else:
                        id_ = self.id_counter
                        self.memo[child_ids_sorted] = id_
                        self.id_counter += 1
                
                self.depth_hashes.setdefault(depth, []).append(id_)
                if stack:
                    stack[-1].append((depth, id_))
                self.pos += 1
            else:
                self.pos += 1
        return depth, id_

s = input().strip()
parser = Parser(s)
depth, _ = parser.parse()
max_depth = max(parser.depth_hashes.keys())
for d in range(1, max_depth + 1):
    d = parser.depth_hashes[d]
    ans = len(set(d))
    print(ans)