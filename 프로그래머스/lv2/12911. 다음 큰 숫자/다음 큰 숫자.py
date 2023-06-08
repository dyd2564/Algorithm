def solution(n):
    answer = n+1
    cnt1 = bin(n).count('1')
    while True:
        cnt2 = bin(answer).count('1')
        if cnt1 == cnt2:
            break
        answer += 1
    return answer