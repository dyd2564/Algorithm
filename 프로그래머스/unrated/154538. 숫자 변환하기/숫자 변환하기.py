from collections import deque
def solution(x, y, n):
    answer = 0
    visit = [-1] * (y+1)
    
    def bfs(x, n):
        q = deque()
        q.append(x)
        visit[x] = 0
        while q:
            v = q.popleft()
            
            if v == y:
                return visit[v]
            
            for nv in (v+n, v*2, v*3):
                if nv <= y and visit[nv] == -1:
                    q.append(nv)
                    visit[nv] = visit[v] + 1
    
        return -1
    
    
    return bfs(x,n)