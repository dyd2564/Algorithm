def solution(park, routes):
    answer = []
    arr = []
    x, y = 0, 0
    for i in range(len(park)):
        a = list(park[i])
        arr.append(a)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == "S":
                x, y = i, j
                arr[i][j] = "O"
                break
    for i in routes:
        dx, dy = 0, 0
        flag = True
        j, k = i.split()
        if j == "E":
            dx, dy = x, y+(1*int(k))
            if 0 <= dx < len(park) and 0 <= dy < len(park[0]):
                for a in range(y, dy+1):
                    if park[dx][a] == "X":
                        flag = False  
                        break
                if flag:
                    x, y = dx, dy
        elif j == "N":
            dx, dy = x-(1*int(k)), y
            if 0 <= dx < len(park) and 0 <= dy < len(park[0]):
                for a in range(dx, x+1):
                    if park[a][dy] == "X":
                        flag = False
                        break
                if flag:
                    x, y = dx, dy
        elif j == "S":
            dx, dy = x+(1*int(k)), y
            if 0 <= dx < len(park) and 0 <= dy < len(park[0]):
                for a in range(x, dx+1):
                    if park[a][dy] == "X":
                        flag = False     
                        break
                if flag:
                    x, y = dx, dy
        elif j == "W":
            dx, dy = x, y-(1*int(k))
            if 0 <= dx < len(park) and 0 <= dy < len(park[0]):
                for a in range(dy, y+1):
                    if park[dx][a] == "X":
                        flag = False   
                        break
                if flag:
                    x, y = dx, dy
    
    return [x, y]