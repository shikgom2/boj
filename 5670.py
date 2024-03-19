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
            return []

    return _find_words_in_subtrie(current_node)
'''
def starts_with(trie, prefix):
    current_node = trie
    for char in prefix:
        if char in current_node:
            current_node = current_node[char]
        else:
            return False
    return True
'''

def _find_words_in_subtrie(subtrie, words=None):
    if words is None:
        words = []

    for key, node in subtrie.items():
        if key == '*':
            words.append(node)
        else:
            _find_words_in_subtrie(node, words)
    return words


while(True):
    try:
        trie = {}    
        a = int(input())
        li = []
        for _ in range(a):
            s = input().strip()
            insert(trie, s)
            li.append(s)

        sum = 0
        idx = 0
        for s in li:
            cnt = 0
            for i in range(1, len(s)+1):
                tmp = s[0:i]
                #print(tmp)
                #print(starts_with(trie, tmp))
                
                if(i == 1):
                    cnt += 1
                    idx = len(starts_with(trie, tmp))
                else:
                    if(idx != len(starts_with(trie, tmp))):
                        cnt += 1
                        idx = len(starts_with(trie, tmp))
            sum += cnt
        print(f"{sum/a:.2f}")
    except:
        break