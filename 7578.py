def init(n):
    size = 1
    while size < n:
        size *= 2
    size = 2 * size - 1
    return [0] * size

def update(tree, idx, start, end, pos, value):
    if start == end:
        tree[idx] += value
    else:
        mid = (start + end) // 2
        if pos <= mid:
            update(tree, 2 * idx + 1, start, mid, pos, value)
        else:
            update(tree, 2 * idx + 2, mid + 1, end, pos, value)
        tree[idx] = tree[2 * idx + 1] + tree[2 * idx + 2]

def query(tree, idx, start, end, qstart, qend):
    if qstart > end or qend < start:
        return 0
    if qstart <= start and qend >= end:
        return tree[idx]
    mid = (start + end) // 2
    left_query = query(tree, 2 * idx + 1, start, mid, qstart, qend)
    right_query = query(tree, 2 * idx + 2, mid + 1, end, qstart, qend)
    return left_query + right_query

def coordinate_compress(arr):
    sorted_unique = sorted(set(arr))
    rank = {val: idx for idx, val in enumerate(sorted_unique)}
    return [rank[x] for x in arr], rank

def count_cross_inversions(a, b):
    combined = a + b
    compressed_combined, rank = coordinate_compress(combined)
    max_val = max(compressed_combined)
    seg_tree = init(max_val + 1)
    inv_count = 0
    cross_pairs = []

    b_compressed = [rank[x] for x in b]
    a_compressed = [rank[x] for x in a]
    
    b_positions = {}
    for i, val in enumerate(b_compressed):
        update(seg_tree, 0, 0, max_val, val, 1)
        if val not in b_positions:
            b_positions[val] = []
        b_positions[val].append(i)

    for i, val in enumerate(a_compressed):
        num_greater_in_b = query(seg_tree, 0, 0, max_val, val + 1, max_val)
        inv_count += num_greater_in_b
        for greater_val in range(val + 1, max_val + 1):
            if greater_val in b_positions:
                for pos in b_positions[greater_val]:
                    cross_pairs.append(((a[i], 'A', i), (b[pos], 'B', pos)))
    
    return inv_count, cross_pairs

# 입력 받기
n = int(input())
li1 = list(map(int, input().split()))
li2 = list(map(int, input().split()))

inv_count, cross_pairs = count_cross_inversions(li1, li2)
print("Number of cross inversions:", inv_count)
print("Cross inversion pairs:")
for pair in cross_pairs:
    print(pair)