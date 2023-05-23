N = int(input())
sum_Arr = []
for i in range(1, N+1):
    arr = list(map(int, str(i)))
    ans = i + sum(arr)
    if ans == N:
        sum_Arr.append(i)
if len(sum_Arr) == 0:
    a = 0
else:
    a = min(sum_Arr)
print(a)