def solution(land):
    for x in range(1, len(land)):
        for y in range(4):
            a = land[x-1][y]
            land[x-1][y] = -10
            land[x][y] += max(land[x-1][0], land[x-1][1], land[x-1][2], land[x-1][3])
            land[x-1][y] = a
    return max(land[x][0], land[x][1], land[x][2], land[x][3])
        

