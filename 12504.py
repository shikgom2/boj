import ipaddress

class TrieNode:
    def __init__(self):
        self.data = None
        self.child = [None, None]

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, network):
        s = network.prefixlen
        current = self.root
        for i in range(s):
            k = (int(network.network_address.packed[i // 8]) >> (7 - i % 8)) & 1
            if current.child[k] is None:
                current.child[k] = TrieNode()
            current = current.child[k]
        current.data = network

    def merge(self):
        def dfs(node):
            if node.child[0]:
                dfs(node.child[0])
            if node.child[1]:
                dfs(node.child[1])
            if node.child[0] and node.child[1] and node.child[0].data and node.child[1].data:
                ones = node.child[0].data.prefixlen
                network = ipaddress.ip_network((int(node.child[0].data.network_address), ones - 1), strict=False)
                node.data = network
                node.child = [None, None]

        dfs(self.root)

    def subnet(self):
        subnets = []

        def dfs(node):
            if node.data:
                subnets.append(node.data)
            if node.child[0]:
                dfs(node.child[0])
            if node.child[1]:
                dfs(node.child[1])

        dfs(self.root)
        return subnets

t = int(input().strip())

for i in range(t):
    n = int(input().strip())
    trie = Trie()
    
    for _ in range(n):
        cidr = input().strip()
        network = ipaddress.ip_network(cidr, strict=False)
        trie.insert(network)
    
    trie.merge()
    
    result = [f"Case #{i+1}:"]
    normalized_subnets = trie.subnet()
    normalized_subnets.sort(key=lambda net: (net.network_address, net.prefixlen))
    result.extend(str(network) for network in normalized_subnets)

    for line in result:
        print(line)
