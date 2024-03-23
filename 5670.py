def insert(root, word):
    node = root
    for char in word:
        if char not in node["children"]:
            node["children"][char] = {"child_cnt": 0, "finish": False, "children": {}}
            node["child_cnt"] += 1
        node = node["children"][char]
    node["finish"] = True

def find(root, word):
    node = root
    answer = 0
    for char in word:
        if node is root or node["child_cnt"] > 1 or node["finish"]:
            answer += 1
        node = node["children"][char]
    return answer

def solve(words):
    root = {"child_cnt": 0, "finish": False, "children": {}}
    for word in words:
        insert(root, word)

    total_strokes = sum(find(root, word) for word in words)
    avg = total_strokes / len(words)
    return avg

while True:
    try:
        n = int(input())
        trie = []
        for _ in range(n):
            s = input()
            trie.append(s)

        print(f"{solve(trie):.2f}")
    except:
        break