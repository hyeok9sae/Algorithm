# 네트워크
def dfs(v, computers, visited, n):
    visited[v] = True
    # for i in range(v+1, i)
    # 무방향 그래프 라서 v+1 부터 탐색ㅎ하려 했으나
    # 탐색하지 못하는 정점이 있어 방문체크를 하지 못해 
    # 다음 싸이클에서 answer가 더해지는 경우가 발생
    for i in range(n):
        if computers[v][i] == 1 and not visited[i]:
            dfs(i, computers, visited, n)

def solution(n, computers):
    answer = 0
    visited = [False]*n
    for i in range(n):
        if not visited[i]:
            dfs(i, computers, visited, n)
            answer += 1
    # print(answer)
    return answer

# solution(6, [[1, 0, 1, 1, 0, 0], [0, 1, 0, 0, 1, 1], [1, 0, 1, 1, 1, 1], [1, 0, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1]])