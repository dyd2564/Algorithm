n, m = map(int, input().split())
arr = []
num = [i+1 for i in range(n)]

def dfs(cnt):
    if cnt == m:
        print(*arr)
        return
    for i in range(n):
        if num[i] not in arr:
            arr.append(num[i])
            dfs(cnt+1)
            arr.pop()
dfs(0)