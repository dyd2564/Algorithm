def solution(brown, yellow):
    answer = []
    total = brown + yellow
    width, height = 0, 0
    for i in range(total, 0, -1):
        if total % i == 0:
            width = i
            height = total // i
            if (width - 2) * (height - 2) == yellow:
                answer.append((width, height))
                break
    return answer[0]