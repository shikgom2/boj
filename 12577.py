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

t = int(input())
for sss in range(t):
    trie = {}
    dic = {}
    cnt = 0
    
    n,m = map(int, input().split())
    for _ in range(n):
        s = input().rstrip()
        li = s.split('/')
        convert = []
        for i in range(1, len(li)):
            if(li[i] in dic):
                convert.append(dic[li[i]])
            else:
                cnt += 1
                dic[li[i]] = cnt
                convert.append(dic[li[i]])
        insert(trie, convert)

    ans = 0
    for _ in range(m):
        s = input().rstrip()
        li = s.split('/')
        
        convert = []
        for i in range(1, len(li)):
            if(li[i] in dic):
                convert.append(dic[li[i]])
            else:
                cnt += 1
                dic[li[i]] = cnt
                convert.append(dic[li[i]])
                
        for i in range(len(convert)):
            tmp = convert[:i+1]
            if (starts_with(trie, tmp) == False):
                ans += 1
                insert(trie, tmp)
                
    print(f"Case #{sss+1}: {ans}")