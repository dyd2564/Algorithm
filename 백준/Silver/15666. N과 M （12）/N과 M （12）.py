n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
arr = []
def dfs(idx, cnt):
    if cnt == m:
        print(*arr)
        return
    check = 0
    for i in range(idx, n):
        if check != num[i]:
            arr.append(num[i])
            check = num[i]
            dfs(i, cnt+1)
            arr.pop()
dfs(0, 0)