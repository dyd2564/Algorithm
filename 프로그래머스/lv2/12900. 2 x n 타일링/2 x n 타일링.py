def solution(n):
    answer = 0
    
    a1 = 1
    a2 = 2
    cnt = 2
    while cnt != n:
        answer = a1 + a2
        a1 = a2
        a2 = answer
        cnt += 1
    
    return answer % 1000000007