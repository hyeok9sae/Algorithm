import heapq as hq

def solution(jobs):
    end, time, count, heap = -1, 0, 0, []
    answer = 0
    n = len(jobs)
    while count < n:
        for i, j in jobs:
            if end < i <= time:
                answer += time - i
                hq.heappush(heap, j)
        if len(heap) > 0:
            answer += len(heap) * heap[0]
            end = time
            time += hq.heappop(heap)
            count += 1
        else:
            time += 1
    # print(answer // n)
    return answer // n


# jobs = [[0, 3], [1, 9], [2, 6]]
# solution(jobs)