def solution(arr):
    stack = []
    i = 0
    
    while i != len(arr):
        if len(stack) == 0:
            stack.append(arr[i])
            i += 1
        elif stack[-1] < arr[i]:
            stack.append(arr[i])
            i += 1
        else:
            stack.pop()
            
    
    
    return stack