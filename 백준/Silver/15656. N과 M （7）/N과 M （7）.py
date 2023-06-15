n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
arr = []

def dfs(cnt):

    if cnt == m:
        print(*arr)
        return
    for i in range(n):
        arr.append(num[i])
        dfs(cnt+1)
        arr.pop()
dfs(0)