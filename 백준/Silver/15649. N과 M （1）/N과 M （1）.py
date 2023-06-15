n, m = map(int, input().split())
arr = []
num = [i for i in range(1, n+1)]

def dfs(cnt):
    if cnt == m:
        print(*arr)
        return
    for i in num:
        if i not in arr:
            arr.append(i)
            dfs(cnt+1)
            arr.pop()
dfs(0)    