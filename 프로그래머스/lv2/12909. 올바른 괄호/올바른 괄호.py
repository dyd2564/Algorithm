def solution(s):
    answer = True
    arr = []
    for i in s:
        if i == '(':
            arr.append(i)
        elif i == ')' and len(arr) > 0:
            arr.pop()
        else:
            return False
    if len(arr) > 0:
        answer = False
    else:
        answer = True
    
    
    

    return answer