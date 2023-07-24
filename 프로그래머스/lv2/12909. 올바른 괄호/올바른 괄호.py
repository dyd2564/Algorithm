from collections import deque

def solution(s):
    answer = True
    q = deque(s)
    stack = []
    
    if q[0] == ')':
        return False
    else:
        while q:
            a = q.popleft()
            if a == '(':
                stack.append(a)
            else: # ) 일때
                if stack:
                    stack.pop()
                else:
                    return False
    if stack or q:
        return False
    
    

    return True