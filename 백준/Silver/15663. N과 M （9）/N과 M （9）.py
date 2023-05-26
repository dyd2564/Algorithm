n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
arr = []
visited = [0] * n
def dfs(cnt, arr, visited):
    if cnt == m:
        print(*arr)
        return
    check = 0
    for i in range(n):
        if visited[i] == 0 and check != num[i]:
            arr.append(num[i])
            visited[i] = 1
            check = num[i]
            dfs(cnt+1, arr, visited)
            arr.pop()
            visited[i] = 0
dfs(0, arr, visited)
