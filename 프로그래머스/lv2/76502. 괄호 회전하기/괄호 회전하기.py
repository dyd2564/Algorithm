from collections import deque
def solution(s):
    answer = 0
    arr = deque(s)
    
    for _ in range(len(s)):
        ans = []
        arr.append(arr.popleft())
        for i in range(len(arr)):
            if len(ans) > 0:
                if ans[-1] == '[' and arr[i] == ']':
                    ans.pop()
                elif ans[-1] == '(' and arr[i] == ')':
                    ans.pop()
                elif ans[-1] == '{' and arr[i] == '}':
                    ans.pop()
                else:
                    ans.append(arr[i])
            else:
                ans.append(arr[i])
        if len(ans) == 0:
            answer += 1
       

    return answer
 
 