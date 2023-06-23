def solution(my_string, s, e):
    answer = ''
    my_string = list(my_string)
    my_string[s:e+1] = (my_string[s:e+1])[::-1]
    
    for i in my_string:
        answer += i
    return answer