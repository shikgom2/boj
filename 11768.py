import sys
from collections import deque

class Edge:
    __slots__ = ['to', 'rev', 'cap']
    def __init__(self, to, rev, cap):
        self.to = to      # target node
        self.rev = rev    # index of reverse edge in target node's list
        self.cap = cap    # capacity

class Dinic:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.level = [0] * n
        self.it = [0] * n

    def add_edge(self, s, t, cap):
        self.graph[s].append(Edge(t, len(self.graph[t]), cap))
        self.graph[t].append(Edge(s, len(self.graph[s]) - 1, 0))

    def bfs(self, s, t):
        self.level = [-1] * self.n
        self.level[s] = 0
        q = deque()
        q.append(s)
        while q:
            u = q.popleft()
            for e in self.graph[u]:
                if self.level[e.to] < 0 and e.cap:
                    self.level[e.to] = self.level[u] + 1
                    q.append(e.to)
        return self.level[t] != -1

    def dfs(self, u, t, flow):
        if not flow:
            return 0
        if u == t:
            return flow
        for i in range(self.it[u], len(self.graph[u])):
            self.it[u] = i
            e = self.graph[u][i]
            if e.cap and self.level[e.to] == self.level[u] + 1:
                pushed = self.dfs(e.to, t, min(flow, e.cap))
                if pushed:
                    e.cap -= pushed
                    self.graph[e.to][e.rev].cap += pushed
                    return pushed
        return 0

    def max_flow(self, s, t):
        flow = 0
        INF = 10**9
        while self.bfs(s, t):
            self.it = [0] * self.n
            while (pushed := self.dfs(s, t, INF)):
                flow += pushed
        return flow

s, r, f, t = map(int, input().split())

# Map each state name to a unique id.
stateId = {}
nextId = 0
def getStateId(name):
    if name not in stateId:
        stateId[name] = nextId
        nextId += 1
    return stateId[name]

# Read raw material sites (suppliers)
supplierState = []
supplier_line = input().split()
for st in supplier_line:
    supplierState.append(getStateId(st))

# Read factory sites.
factoryState = []
factory_line = input().split()
for st in factory_line:
    factoryState.append(getStateId(st))

# For each transportation company, record the set of allowed states.
companyAllowed = []
for _ in range(t):
    parts = input().split()
    n = int(parts[0])
    allowed = set()
    for st in parts[1:]:
        allowed.add(getStateId(st))
    companyAllowed.append(allowed)

# Build indices for flow network nodes.
# Nodes:
# source: 0
# suppliers: nodes 1 ... r
# transportation companies: each company is split into two nodes:
#   company_in nodes, then company_out nodes.
# factories, then sink.
source = 0
supplier_start = 1
supplier_end = supplier_start + r - 1

company_in_start = supplier_end + 1
company_count = t
company_in_end = company_in_start + company_count - 1
company_out_start = company_in_end + 1
company_out_end = company_out_start + company_count - 1

factory_start = company_out_end + 1
factory_end = factory_start + f - 1

sink = factory_end + 1
total_nodes = sink + 1

dinic = Dinic(total_nodes)

# Source -> supplier (capacity 1)
for i in range(r):
    dinic.add_edge(source, supplier_start + i, 1)

# Each transportation company: split into in and out with capacity 1.
for i in range(t):
    dinic.add_edge(company_in_start + i, company_out_start + i, 1)

# Supplier -> Company edges.
for i in range(r):
    s_state = supplierState[i]
    supplier_node = supplier_start + i
    for j in range(t):
        if s_state in companyAllowed[j]:
            comp_in = company_in_start + j
            dinic.add_edge(supplier_node, comp_in, 1)

# Company -> Factory edges.
for j in range(t):
    comp_out = company_out_start + j
    for i in range(f):
        f_state = factoryState[i]
        if f_state in companyAllowed[j]:
            factory_node = factory_start + i
            dinic.add_edge(comp_out, factory_node, 1)

# Company -> Company edges.
# For each ordered pair of companies (i, j), if they share at least one state.
for i in range(t):
    comp_out_i = company_out_start + i
    for j in range(t):
        if i == j:
            continue
        # if companies i and j share a state, add an edge from i_out to j_in.
        if companyAllowed[i] & companyAllowed[j]:
            comp_in_j = company_in_start + j
            dinic.add_edge(comp_out_i, comp_in_j, 1)

# Factory -> Sink edges.
for i in range(f):
    factory_node = factory_start + i
    dinic.add_edge(factory_node, sink, 1)

max_supplied = dinic.max_flow(source, sink)
print(max_supplied)
