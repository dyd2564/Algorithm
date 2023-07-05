from collections import deque
v = int(input())
e = int(input())

graph = [[] for i in range(v+1)]
for i in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (v+1)
# def bfs(start):
#     q = deque([start])
#     cnt = 0
#     visited[start] = 1
#     while q:
#         n = q.popleft()
#         for nx in graph[n]:
#             if visited[nx] == 0:
#                 visited[nx] = 1
#                 q.append(nx)
#                 cnt += 1
#     return cnt
# print(bfs(1))
cnt = 0
def dfs(start):
    visited[start] = 1
    global cnt
    cnt += 1
    for nx in graph[start]:
        if visited[nx] == 0:
            visited[nx] = 1
            dfs(nx)
    return cnt

print(dfs(1)-1)