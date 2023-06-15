def solution(cacheSize, cities):
    answer = 0
    cache = []
    for i in range(len(cities)):
        cities[i] = cities[i].lower()
        if cities[i] not in cache:
            if len(cache) < cacheSize:
                cache.append(cities[i])
            else:
                cache.append(cities[i])
                cache.pop(0)
            answer += 5
        else:
            cache.pop(cache.index(cities[i]))
            cache.append(cities[i])
            answer += 1
    return answer