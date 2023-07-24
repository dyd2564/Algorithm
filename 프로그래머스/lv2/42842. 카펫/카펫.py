def solution(brown, yellow):
    answer = []
    total = brown + yellow
    width, height = 0, 0
    for i in range(total, 1, -1):
        if total % i == 0:
            height = total//i
            width = i
            if (height-2)*(width-2) == yellow:
                return [width, height]
    