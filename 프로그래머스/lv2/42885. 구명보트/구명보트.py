from collections import deque
def solution(people, limit):
    answer = 0
    q = deque(sorted(people, reverse=True))
    while q:
        if len(q) > 1 and q[0] + q[-1] <= limit:
            q.popleft()
            q.pop()
        else:
            if q and q[0] <= limit:
                q.popleft()
        answer += 1
    return answer