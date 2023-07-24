from collections import Counter
def solution(k, tangerine):
    tangerines = Counter(tangerine)
    tangerines = sorted(tangerines.values(), reverse=True)
    cnt, answer = 0, 0
    for i in tangerines:
        cnt += i
        answer += 1
        if cnt >= k:
            return answer
