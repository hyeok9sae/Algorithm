# 특정한 최단 경로
import heapq

def dijkstra(start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    que = []
    heapq.heappush(que, [start, distances[start]])
    while que:
        cur_dest, cur_dist = heapq.heappop(que)
        if distances[cur_dest] < cur_dist:
            continue
        for new_dest, new_dist in graph[cur_dest].items():
            dist = cur_dist + new_dist
            if dist < distances[new_dest]:
                distances[new_dest] = dist
                heapq.heappush(que, [new_dest, dist])
    return distances

N, E = map(int, input().split())
graph = {i:{} for i in range(1, N+1)}
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c
v1, v2 = map(int, input().split())
res1 = dijkstra(1)[v1]+dijkstra(v1)[v2]+dijkstra(v2)[N]
res2 = dijkstra(1)[v2]+dijkstra(v2)[v1]+dijkstra(v1)[N]
answer = min(res1, res2)
print(answer if answer < float('inf') else -1)