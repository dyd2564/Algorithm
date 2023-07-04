import sys
sys.setrecursionlimit(10**5)
# input = sys.stdin.readline()

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 상우하좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y):
    graph[x][y] = 0
    global cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < n) and (0 <= ny < n) and graph[nx][ny] == 1:
            cnt += 1
            dfs(nx, ny)



cnt_arr = []
for x in range(n):
    for y in range(n):
        if graph[x][y] == 1:
            cnt = 1
            dfs(x, y)
            cnt_arr.append(cnt)

cnt_arr.sort()
print(len(cnt_arr))
for i in cnt_arr:
    print(i)
