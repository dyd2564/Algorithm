def solution(want, number, discount):
    answer = 0
    wants = []
    for v, n in zip(want, number):
        wants += [v]*n
    wants.sort()
    # print(wants)
    for i in range(len(discount)-9):
        if sorted(discount[i:i+10]) == wants:
            answer += 1
            # print(sorted(discount[i:i+10])
            # print(discount[i:i+10])
    
    return answer