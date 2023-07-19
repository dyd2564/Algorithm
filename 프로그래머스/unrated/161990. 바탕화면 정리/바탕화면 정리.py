def solution(wallpaper):
    answer = []
    left = []
    right = []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                left.append(i)
                right.append(j)
    
    return [min(left), min(right), max(left)+1, max(right)+1]