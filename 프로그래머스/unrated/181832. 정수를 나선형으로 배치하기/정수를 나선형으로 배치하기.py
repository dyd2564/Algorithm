def solution(n):
    answer = [[0] * n for _ in range(n)]

    # 우 하 좌 상
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    i = 0
    x, y = 0, 0
    answer[0][0] = 1
    start = 2
    while start < n * n+1:

        x += dx[i]
        y += dy[i]

        if 0 <= x < n and 0 <= y < n and answer[x][y] == 0:
            answer[x][y] = start
            start += 1
        else:
            x -= dx[i]
            y -= dy[i]
            i += 1

            if i == 4:
                i = 0

    return answer