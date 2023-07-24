from collections import deque
def solution(s):
    answer = -1
    
    q = deque(s)
    stack = []
    
    while q:
        a = q.popleft()
        if stack and stack[-1] == a:
            stack.pop()
        else:
            stack.append(a)
    if q or stack:
        return 0
    else:
        return 1
            
            
        
    
    


    return answer