def solution(cacheSize, cities):
    answer = 0
    cache_hit = 1
    cache_miss = 5
    cache = {}
    time = 0
    for i in cities:
        i = i.upper()
        if cacheSize == 0:
            answer += cache_miss
            continue
        if len(cache) < cacheSize:
            if i in cache:
                cache[i] = time
                answer += cache_hit
            else:
                cache[i] = time
                answer += cache_miss
        else:
            if i in cache:
                cache[i] = time
                answer += cache_hit
            else:
                key_min = min(cache.keys(), key= lambda x: cache[x])
                del cache[key_min]
                cache[i] = time
                answer += cache_miss
        time += 1
    # print(answer)
    return answer

# cacheSize = 1
# cities = ["sad", "sad", "sad"]
# solution(cacheSize, cities)