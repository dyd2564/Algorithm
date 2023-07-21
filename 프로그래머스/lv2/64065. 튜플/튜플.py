def solution(s):
    answer = []
    a = s[2:-2].split('},{')
    a.sort(key = lambda x:len(x))
    for i in a:
        for j in i.split(','):
            if int(j) not in answer:
                answer.append(int(j))
    return answer