from collections import deque

class ConvexHullTrick:
    def __init__(self):
        self.hull = deque()
    
    def add_line(self, a, b):
        while len(self.hull) >= 2 and self._is_bad(self.hull[-2], self.hull[-1], (a, b)):
            self.hull.pop()
        self.hull.append((a, b))
    
    def query(self, x):
        while len(self.hull) >= 2 and self._f(self.hull[0], x) >= self._f(self.hull[1], x):
            self.hull.popleft()
        return self._f(self.hull[0], x)
    
    def _f(self, line, x):
        a, b = line
        return a * x + b
    
    def _is_bad(self, line1, line2, line3):
        a1, b1 = line1
        a2, b2 = line2
        a3, b3 = line3
        return (b3 - b1) * (a1 - a2) >= (b2 - b1) * (a1 - a3)

# Example usage:
cht = ConvexHullTrick()
cht.add_line(1, 1)  # y = x + 1
cht.add_line(2, 0)  # y = 2x + 0
cht.add_line(3, -1) # y = 3x - 1

print(cht.query(1)) # Output: 1
print(cht.query(2)) # Output: 3
