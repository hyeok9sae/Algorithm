def solution(bridge_length, weight, truck_weights):
    answer = 0
    lst = [0]*bridge_length
    while lst:
        answer += 1
        lst.pop(0)
        if truck_weights:
            if sum(lst) + truck_weights[0] <= weight:
                lst.append(truck_weights.pop(0))
            else:
                lst.append(0)
    # print(answer)
    return answer

# bridge_length = 2
# weight = 10
# truck_weights = [7, 4, 5, 6]
# solution(bridge_length, weight, truck_weights)