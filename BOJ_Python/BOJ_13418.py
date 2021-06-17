# 학교 탐방하기
def make_set(v):
    parent[v] = v
    rank[v] = 0

def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]

def union(v1, v2):
    root1 = find(v1)
    root2 = find(v2)
    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1

def kruskal(vertax, edge, flag):
    mst = [] 
    for v in vertax:
        make_set(v)
    edges = edge
    if flag:
        edges.sort(key=lambda x:x[2])
    else:
        edges.sort(key=lambda x:x[2], reverse=True)
    for e in edges:
        v1, v2, cost = e
        if find(v1) != find(v2):
            union(v1, v2)
            mst.append(cost)
    return mst

N, M = map(int, input().split())
edge = []
vertax = [i for i in range(N+1)]
for _ in range(M+1):
    a, b, c = map(int, input().split())
    edge.append([a, b, c])
parent, rank = {}, {}
mst1 = kruskal(vertax, edge, True)
parent, rank = {}, {}
mst2 = kruskal(vertax, edge, False)
print(abs(mst1.count(0)*mst1.count(0) - mst2.count(0)*mst2.count(0)))