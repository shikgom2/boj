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

def _find_words_in_subtrie(subtrie, words=None):
    if words is None:
        words = []

    for key, node in subtrie.items():
        if key == '*':
            words.append(node)
        else:
            _find_words_in_subtrie(node, words)
    return words

t = int(input())
for _ in range(t):
    trie = {}
    i = int(input())
    li = []
    for _ in range(i):
        s =input()
        insert(trie, s)
        li.append(s)

    flag = True
    for i in li:
        if(len(starts_with(trie, i)) >= 2):
            print("NO")
            flag = False
            break
    if(flag):   
        print("YES")
