def solution(array, commands):
    answer = []
    for command in commands:
        a, b, c = command
        answer.append(sorted(array[a-1:b])[c-1])
    return answer