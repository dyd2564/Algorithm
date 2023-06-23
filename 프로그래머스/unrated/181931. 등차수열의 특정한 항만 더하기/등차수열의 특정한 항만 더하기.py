def solution(a, d, included):
    answer = 0
    while included:
        if included[0] == True:
            answer += a
        a += d
        included.pop(0)
    return answer