from collections import deque
def solution(progresses, speeds):
    answer = []
    p_q = deque(progresses)
    s_q = deque(speeds)
    cnt, time = 0, 0
    while p_q:
        if p_q[0] + time*s_q[0] >= 100:
            p_q.popleft()
            s_q.popleft()
            cnt += 1
        else:
            if cnt > 0:
                answer.append(cnt)
                cnt = 0
            time += 1
    answer.append(cnt)
                    
        
    return answer