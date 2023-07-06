from collections import deque
def solution(numbers, target):
    answer = 0
    q = deque()
    q.append((0, 0))
    
    while q:
        s, l = q.popleft()
        
        if l == len(numbers):
            if s == target:
                answer += 1
        else:
            q.append((s + numbers[l], l+1))
            q.append((s - numbers[l], l+1))
    
    return answer