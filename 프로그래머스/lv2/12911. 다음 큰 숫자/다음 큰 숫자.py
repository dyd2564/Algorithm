def solution(n):
    a1 = bin(n)[2:].count('1')
    answer = n+1
    while True:
        a2 = bin(answer)[2:].count('1')
        if a1 == a2:
            break
        answer += 1
    return answer