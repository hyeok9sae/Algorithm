import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    for i in scoville:
        heapq.heappush(heap, i)
    while len(heap) > 1:
        a = heapq.heappop(heap)
        if a >= K:
            heapq.heappush(heap, a)
            break
        b = heapq.heappop(heap)
        heapq.heappush(heap, a + (b*2))
        answer += 1
    if heapq.heappop(heap) < K:
        answer = -1
    # print(answer)
    return answer

# scoville = [1, 2, 3, 9, 10, 12]
# K = 7
# solution(scoville, K)