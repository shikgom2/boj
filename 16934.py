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
            return []

    return _find_words_in_subtrie(current_node)

def _find_words_in_subtrie(subtrie, prefix='', words=None):
    if words is None:
        words = []

    for key, node in subtrie.items():
        if key == '*':
            words.append(prefix)
        else:
            _find_words_in_subtrie(node, prefix + key, words)
    return words

trie = {}
d = {}
i = int(input())
for _ in range(i):
    s =input()
    insert(trie, s)

    for l in range(1, len(s)):
        tmp = s[0:l]
        print(tmp, starts_with(trie, tmp))
        if(len(starts_with(trie, tmp)) == 1 and tmp not in d):
            print(tmp)
            d[tmp] = 1
            break