cnt = 1
stack = []
arr = []
temp = True
n = int(input())
for _ in range(n):
    a = int(input())

    while cnt <= a:
        stack.append(cnt)
        arr.append('+')
        cnt += 1
    if stack[-1] == a:
        stack.pop()
        arr.append('-')
    else:
        temp = False
        break
if temp == False:
    print('NO')
else:
    for i in arr:
        print(i)


