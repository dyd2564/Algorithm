from collections import deque
def solution(priorities, location):
    answer = 0
    arr = [i for i in range(len(priorities))] # 0 1 2 3
    q = deque(priorities) # 3 2 2 1
    p = deque(arr) # 2 3 0 1
    ans = []
    cnt = 0
    while q:
        max_q = max(q)
        if q[0] != max_q:
            p.append(p.popleft())
            q.append(q.popleft())
        else:
            cnt += 1
            q.popleft()
            if p.popleft() == location:
                break
            
            
    return cnt