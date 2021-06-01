# 행성 터널
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

N = int(input())
tmp = []
for i in range(N):
    x, y, z = map(int, input().split())
    tmp.append([x, y, z, i+1])
graph = []
mst = []
parent, rank = {}, {}
for i in range(N+1):
    make_set(i)
# 모든 간선을 구하면(v*(v-1)/2) 메모리초과 이다.
# x, y, z축 별로 각각 정렬하여 간선을 구하면 3*(v-1)개 이므로 메모리가 줄어든다.
for i in range(3):
    tmp.sort(key=lambda x: x[i])
    for j in range(len(tmp)-1):
        graph.append([tmp[j+1][i]-tmp[j][i], tmp[j+1][3], tmp[j][3]])
graph.sort()
# print(graph)
for i in graph:
    if find(i[1]) != find(i[2]):
        union(i[1], i[2])
        mst.append(i)
ans = 0
for i in mst:
    ans += i[0]
print(ans)
# # print(graph)