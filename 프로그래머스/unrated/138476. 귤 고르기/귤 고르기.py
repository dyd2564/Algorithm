from collections import Counter
def solution(k, tangerine):
    answer = 0
    arr = Counter(tangerine)
    
    arr = sorted(arr.values(), reverse=True)
    
    cnt = 0
    
    for i in arr:
        answer += i
        cnt += 1
        if answer >= k:
            break
        
    
    return cnt