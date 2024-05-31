import sys
input = sys.stdin.readline

class AhoCorasick:
    def __init__(self, patterns):
        self.trie = {}
        self.patterns = patterns
        self.output = {}
        self.fail = {}
        self.node_count = 0
        self.create_trie()
        self.create_failure_links()

    def create_trie(self):
        """Creates the trie from the patterns."""
        for pattern in self.patterns:
            current_node = self.trie
            for char in pattern:
                if char not in current_node:
                    self.node_count += 1
                    current_node[char] = {'_id': self.node_count}
                current_node = current_node[char]
            current_node['output'] = current_node.get('output', []) + [pattern]

    def create_failure_links(self):
        """Creates failure links for the Aho-Corasick automaton."""
        import collections
        queue = collections.deque()
        
        # Initialize the queue with depth 1 nodes and set their fail links to root
        for char in self.trie:
            if char != 'output':
                self.fail[self.trie[char]['_id']] = self.trie
                queue.append(self.trie[char])
        
        # BFS to create fail links
        while queue:
            current_node = queue.popleft()
            current_node_id = current_node['_id']
            
            for char, next_node in current_node.items():
                if char == 'output' or char == '_id':
                    continue
                
                next_node_id = next_node['_id']
                queue.append(next_node)
                
                fail_state = self.fail[current_node_id]
                while char not in fail_state and fail_state != self.trie:
                    fail_state = self.fail[fail_state['_id']]
                
                self.fail[next_node_id] = fail_state.get(char, self.trie)
                if 'output' in self.fail[next_node_id]:
                    next_node['output'] = next_node.get('output', []) + self.fail[next_node_id]['output']

    def search(self, text):
        """Searches the patterns in the given text."""
        current_node = self.trie
        occurrences = {}
        for i in range(len(text)):
            char = text[i]
            while char not in current_node and current_node != self.trie:
                current_node = self.fail[current_node['_id']]
            current_node = current_node.get(char, self.trie)
            
            if 'output' in current_node:
                for pattern in current_node['output']:
                    if pattern not in occurrences:
                        occurrences[pattern] = []
                    occurrences[pattern].append(i - len(pattern) + 1)
        
        return occurrences
    

n = int(input())
target = input().rstrip()

patterns = []
n = int(input())
for _ in range(n):
    s = input().rstrip()
    patterns.append(s)

ac = AhoCorasick(patterns)
res = ac.search(target)

ans = [0] * len(target)
s = len(target)

#found
if res:
    
    patterns = []
    #가장 긴 pattern만 판단
    for pattern, positions in res.items():
        #print(f"Pattern '{pattern}' found {len(positions)} times at positions: {positions}")
        
        for i in range(int(positions[0]), int(positions[0]) + len(pattern)):
            if(ans[i] == 0):
                ans[i] = 1
                s -= 1           
    print(s)
else:
    print(len(ans))