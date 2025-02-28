def solve():
    INF = 10**18
    n = int(input())
    A = list(map(int, input().split()))
    
    # Fenwick Tree (구간 합 S 관리)
    class Fenw:
        def __init__(self, n):
            self.n = n
            self.fw = [0]*(n+1)
        def update(self, i, delta):
            i += 1
            while i <= self.n:
                self.fw[i] += delta
                i += i & -i
        def query(self, i):
            s = 0
            i += 1
            while i:
                s += self.fw[i]
                i -= i & -i
            return s
        def range_query(self, l, r):
            return self.query(r) - (self.query(l-1) if l > 0 else 0)
    
    fenw = Fenw(n)
    for i in range(n):
        fenw.update(i, A[i])
    
    # 두 배열 – tree_B와 tree_C 구성
    # tree_B: 인덱스가 홀수일 때 사용 (B[i] = A[i] if (i+1) odd, else -A[i])
    # tree_C: 인덱스가 짝수일 때 사용 (C[i] = A[i] if (i+1) even, else -A[i])
    B_arr = [0] * n
    C_arr = [0] * n
    for i in range(n):
        if (i+1) & 1:
            B_arr[i] = A[i]
            C_arr[i] = -A[i]
        else:
            B_arr[i] = -A[i]
            C_arr[i] = A[i]
    
    # 세그먼트 트리 구축 (구간 [l, r]에 대해 교대 prefix 합, 최소 홀수 prefix, 최대 짝수 prefix 등 관리)
    size = 1
    while size < n:
        size *= 2

    # identity (빈 구간) : 길이 0, 총합 0, 홀수 prefix는 INF, 짝수 prefix의 최대는 0
    identity = (0, float('inf'), 0, 0)  # (total, best_odd, best_even, length)
    
    # 단일 구간(길이 1)에서는 prefix는 [0, x]가 되어야 함.
    def make_node(x):
        return (x, x, 0, 1)
    
    # 두 노드를 합칠 때, 왼쪽 구간의 길이가 홀수이면 오른쪽 구간의 인덱스 패리티가 바뀜.
    def combine(left, right):
        total = left[0] + right[0]
        if left[3] & 1:
            r_odd = right[2]
            r_even = right[1]
        else:
            r_odd = right[1]
            r_even = right[2]
        best_odd = min(left[1], left[0] + r_odd)
        best_even = max(left[2], left[0] + r_even)
        return (total, best_odd, best_even, left[3] + right[3])
    
    tree_B = [identity] * (2 * size)
    tree_C = [identity] * (2 * size)
    for i in range(n):
        tree_B[size + i] = make_node(B_arr[i])
        tree_C[size + i] = make_node(C_arr[i])
    for i in range(n, size):
        tree_B[size + i] = identity
        tree_C[size + i] = identity
    for i in range(size - 1, 0, -1):
        tree_B[i] = combine(tree_B[2 * i], tree_B[2 * i + 1])
        tree_C[i] = combine(tree_C[2 * i], tree_C[2 * i + 1])
    
    def update_tree(tree, pos, val):
        i = pos + size
        tree[i] = make_node(val)
        i //= 2
        while i:
            tree[i] = combine(tree[2 * i], tree[2 * i + 1])
            i //= 2
    
    def query_tree(tree, l, r):
        l += size
        r += size
        res_left = identity
        res_right = identity
        while l <= r:
            if l & 1:
                res_left = combine(res_left, tree[l])
                l += 1
            if not (r & 1):
                res_right = combine(tree[r], res_right)
                r -= 1
            l //= 2
            r //= 2
        return combine(res_left, res_right)
    
    q = int(input())
    for _ in range(q):
        parts = input().split()
        if parts[0] == '1':
            i = int(parts[1])
            v = int(parts[2])
            idx = i - 1
            delta = v - A[idx]
            A[idx] = v
            fenw.update(idx, delta)
            if i & 1:
                update_tree(tree_B, idx, v)
                update_tree(tree_C, idx, -v)
            else:
                update_tree(tree_B, idx, -v)
                update_tree(tree_C, idx, v)
        else:
            l = int(parts[1])
            r = int(parts[2])
            l0 = l - 1
            r0 = r - 1
            m = r - l + 1
            S_val = fenw.range_query(l0, r0)
            # l번째 도시가 홀수이면 tree_B, 짝수이면 tree_C 사용 (재인덱싱 시 첫 원소를 홀수 위치로)
            if l & 1:
                seg = query_tree(tree_B, l0, r0)
            else:
                seg = query_tree(tree_C, l0, r0)
            total_alt, best_odd, best_even, _ = seg
            if m & 1:  # 구간 길이가 홀수인 경우
                if total_alt & 1:
                    print(-1)
                    continue
                X = total_alt // 2
                if X > best_odd or X < best_even:
                    print(-1)
                    continue
                ans = (S_val - m * X) // 2
                print(ans)
            else:  # 구간 길이가 짝수인 경우
                if total_alt != 0 or best_odd < best_even:
                    print(-1)
                    continue
                X = best_odd
                ans = (S_val - m * X) // 2
                print(ans)

if __name__ == '__main__':
    solve()
