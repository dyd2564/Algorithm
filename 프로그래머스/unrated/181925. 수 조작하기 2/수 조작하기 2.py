from collections import deque
def solution(numLog):
    answer = ''
    q = deque(numLog)
    while len(q) > 1:
        num1 = q[0]
        num2 = q[1]
        diff = num2 - num1
        if diff == 1:
            answer += 'w'
        elif diff == -1:
            answer += 's'
        elif diff == 10:
            answer += 'd'
        else:
            answer += 'a'
        q.popleft()
    return answer