def solution(arr):
    stack = []
    
    i = 0
    while i < len(arr):
        
        if not stack:
            stack.append(arr[i])
            i += 1
        elif stack and stack[-1] == arr[i]:
            stack.pop()
            i += 1
        elif stack and stack[-1] != arr[i]:
            stack.append(arr[i])
            i += 1
            
    if not stack:
        return [-1]
    return stack