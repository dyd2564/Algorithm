def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs:
        if int(str(i)[s:s+l]) > k:
            answer.append(int(str(i)[s:s+l]))
    return answer