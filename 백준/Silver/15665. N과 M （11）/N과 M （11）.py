n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
arr = []

def dfs(cnt):
    if cnt == m:
        print(*arr)
        return
    check = 0
    for i in range(n):
        if num[i] != check:
            arr.append(num[i])
            check = num[i]
            dfs(cnt+1)
            arr.pop()
dfs(0)