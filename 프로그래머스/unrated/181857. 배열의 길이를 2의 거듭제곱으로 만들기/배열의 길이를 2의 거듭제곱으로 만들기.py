def solution(arr):
    answer = arr
    a = len(arr)
    cnt = 0
    while a != 1:
        if a % 2 == 0:
            a /= 2
        else:
            cnt += 1
            a = len(arr) + cnt
            
    answer += [0] * cnt        
    return answer