import sys
import threading

sys.setrecursionlimit(1 << 25)  # Increase the recursion limit.

def main():
    s = sys.stdin.readline().strip()
    parser = Parser(s)
    depth, _ = parser.parse()
    max_depth = max(parser.depth_hashes.keys())
    for d in range(1, max_depth + 1):
        ids_at_depth = parser.depth_hashes[d]
        num_unique = len(set(ids_at_depth))
        print(num_unique)

class Parser:
    def __init__(self, s):
        self.s = s
        self.n = len(s)
        self.pos = 0
        self.depth_hashes = {}  # Stores hashes at each depth.
        self.memo = {}          # Memoization for subtree hashes.
        self.id_counter = 2     # Unique ID counter starting from 2.
    
    def parse(self):
        if self.s[self.pos] != '(':
            # Invalid input handling.
            pass
        self.pos += 1  # Skip '('
        child_ids = []
        child_depths = []
        while self.pos < self.n and self.s[self.pos] == '(' and len(child_ids) < 3:
            depth, id_ = self.parse()
            child_depths.append(depth)
            child_ids.append(id_)
            
        if self.pos >= self.n or self.s[self.pos] != ')':
            # Invalid input handling.
            pass
        self.pos += 1  # Skip ')'

        if not child_depths:
            # Leaf node (no subordinates).
            depth = 1
            id_ = 1
        else:
            depth = 1 + max(child_depths)
            # Subordinates are unordered; sort their IDs.
            child_ids_sorted = tuple(sorted(child_ids))
            if child_ids_sorted in self.memo:
                id_ = self.memo[child_ids_sorted]
            else:
                id_ = self.id_counter
                self.memo[child_ids_sorted] = id_
                self.id_counter += 1
        # Record the ID at this depth.
        self.depth_hashes.setdefault(depth, []).append(id_)
        return depth, id_

if __name__ == "__main__":
    threading.Thread(target=main).start()
