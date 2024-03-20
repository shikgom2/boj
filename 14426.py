import sys
input = sys.stdin.readline

def insert(trie, string):
    current_node = trie
    for char in string:
        if char not in current_node:
            current_node[char] = {}
        current_node = current_node[char]
    current_node['*'] = string

def search(trie, string):
    current_node = trie
    for char in string:
        if char in current_node:
            current_node = current_node[char]
        else:
            return False
    return '*' in current_node

def starts_with(trie, prefix):
    current_node = trie
    for char in prefix:
        if char in current_node:
            current_node = current_node[char]
        else:
            return False
    return True

def _find_words_in_subtrie(subtrie, words=None):
    if words is None:
        words = []

    for key, node in subtrie.items():
        if key == '*':
            words.append(node)
            return words
        else:
            _find_words_in_subtrie(node, words)
    return words

trie = {}
i,j = map(int, input().split())

for _ in range(i):
    s =input()
    insert(trie, s)

cnt = 0
for _ in range(j):
    s=input().strip()
    if(starts_with(trie, s)):
        cnt += 1

print(cnt)