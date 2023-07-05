def solution(l, r):
    answer = []
    for i in range(l, r+1):
        if i % 5 == 0:
            a = str(i)
            flag = True
            for j in a:
                if int(j) not in [0,5]:
                    flag = False
                    break
            if flag:
                answer.append(int(a))
    if len(answer) == 0:
        return [-1]
    return answer