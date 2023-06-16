from collections import Counter
def solution(k, tangerine):
    answer = 0
    arr = Counter(tangerine)
    arr = sorted(arr.values(), reverse=True)
    cnt = 0
    for i in arr:
        cnt += i
        answer += 1
        if cnt >= k:
            break
    return answer