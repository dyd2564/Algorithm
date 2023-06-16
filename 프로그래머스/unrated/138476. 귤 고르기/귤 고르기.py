from collections import Counter
def solution(k, tangerine):
    sum1 = 0
    arr = Counter(tangerine)
    arr = sorted(arr.values(), reverse=True)
    cnt = 0
    for i in arr:
        sum1 += i
        cnt += 1
        if sum1 >= k:
            break
    return cnt