T = int(input())


for _ in range(T):
    a = input()
    arr = []
    ans = 'YES'
    for i in range(len(a)):
        if a[i] == '(':
            arr.append(a[i])
        else:
            if len(arr) > 0:
                arr.pop()
            else:
                ans = 'NO'
    if len(arr) > 0:
        ans = 'NO'
    print(ans)