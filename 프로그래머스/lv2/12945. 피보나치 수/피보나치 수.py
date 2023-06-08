def solution(n):
    cnt = 2
    a1 = 1
    a2 = 1
    while True:
        a3 = a1 + a2
        a1 = a2
        a2 = a3
        cnt += 1
        if cnt == n:
            break
        
    return a3 % 1234567