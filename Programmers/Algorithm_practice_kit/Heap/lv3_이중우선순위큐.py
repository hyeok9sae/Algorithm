import heapq as hq
def solution(operations):
    answer = []
    heap = []
    for i in operations:
        a, b = map(str, i.split())
        if a == "I":
            hq.heappush(heap, int(b))
        else:
            if len(heap) > 0:
                if b == "1":
                    heap.sort()
                    heap.pop()
                else:
                    hq.heappop(heap)
    if heap:
        answer.append(max(heap))
        answer.append(min(heap))
    else:
        answer.append(0)
        answer.append(0)
    # print(answer)
    return answer

# operations = ["I 7", "I 5", "I -5", "D -1"]
# solution(operations)