def solution(arr, flag):
    answer = []
    
    for i in range(len(arr)):
        if flag[i] == True:
            a = [arr[i]] * (arr[i] * 2)
            answer.extend(a)
        else:
            for j in range(arr[i]):
                answer.pop()
            
    return answer