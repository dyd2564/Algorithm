from collections import deque
def solution(priorities, location):
    answer = 0
    arr = [i for i in range(len(priorities))]
    q = deque(priorities) # 3 2 2 1
    p = deque(arr) # 2 3 0 1
    ans = []
    while q:
        max_q = max(q)
        if q[0] != max_q:
            p.append(p.popleft())
            q.append(q.popleft())
        else:
            q.popleft()
            ans.append(p.popleft())
    return ans.index(location)+1