n, m = map(int, input().split())
arr = []
num = [i+1 for i in range(n)] # 1 2 3 4
def dfs(idx, cnt):
    if cnt == m:
        print(*arr)
        return
    for i in range(idx, n):
        arr.append(num[i])
        dfs(i, cnt+1)
        arr.pop()
dfs(0, 0)