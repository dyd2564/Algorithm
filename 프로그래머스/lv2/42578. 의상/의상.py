def solution(clothes):
    answer = 1
    dic = {}
    for i in clothes:
        if i[1] in dic:
            dic[i[1]] += 1
        else:
            dic[i[1]] = 1
    # print(dic.items())
    for a in dic.values():
        answer *= (a+1)
    return answer - 1