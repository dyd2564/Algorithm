def solution(code):
    answer = ''
    mode = 0
    for i in range(len(code)):
        if code[i] == '1':
            if mode == 1:
                mode = 0
            else:
                mode =1
        else:
            if mode == 0:
                if i % 2 == 0:
                    answer += code[i]
            if mode == 1:
                if i % 2 == 1:
                    answer += code[i]
    if len(answer) == 0:
        return "EMPTY"
    return answer