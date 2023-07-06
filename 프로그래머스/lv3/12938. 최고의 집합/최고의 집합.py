def solution(n, s):
    answer = []
    # 4 10 -> 몫 : 2 나머지 : 2
    # 2, 2, 3, 3
    # 3 10 -> 몫 : 3 나머지 : 1
    # 3, 3, 4
    # 5, 16 -> 몫 : 3 나머지 : 1
    # 3, 3, 3, 3, 4
    
    # 몫 : a, 나머지 : b
    a = s // n
    b = s % n
    if s < n:
        return [-1]
    for i in range(n-b):
        answer.append(a)
    for i in range(b):
        answer.append(a+1)
    return answer