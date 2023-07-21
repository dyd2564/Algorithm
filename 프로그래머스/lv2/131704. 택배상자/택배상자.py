def solution(order):
    sub = []
    i = 1
    cnt = 0
    while i != len(order) + 1:
        sub.append(i)
        while sub and sub[-1] == order[cnt]:
            cnt += 1
            sub.pop()
        i += 1
            
    return cnt