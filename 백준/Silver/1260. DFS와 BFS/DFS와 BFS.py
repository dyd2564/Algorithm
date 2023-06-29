from collections import deque
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()
    
def dfs(v):
    print(v, end=' ')
    
    for nv in graph[v]:
        if visited[nv] == 0:
            visited[nv] = 1
            dfs(nv)
visited[v] = 1
dfs(v)

print()
def bfs(v):
    q = deque()
    q.append(v)
    visited = [0] * (n+1)
    visited[v] = 1
    
    while q:
        v = q.popleft()
        print(v, end=' ')
        
        for nv in graph[v]:
            if visited[nv] == 0:
                visited[nv] = 1
                q.append(nv)
bfs(v)