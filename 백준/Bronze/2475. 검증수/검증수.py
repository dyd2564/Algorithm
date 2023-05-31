arr = list(map(int, input().split()))
a = 0
for i in arr:
    a += i*i
print(a%10)