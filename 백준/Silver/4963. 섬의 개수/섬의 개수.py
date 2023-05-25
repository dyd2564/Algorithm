import sys
sys.setrecursionlimit(10**4)
dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]
def dfs(x, y):
    graph[x][y] = 0
    for k in range(8):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
            dfs(nx, ny)
            

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)