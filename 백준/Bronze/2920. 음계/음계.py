arr = [i for i in range(1, 9)]
a = list(map(int, input().split()))
if a == arr:
    print('ascending')
elif a == arr[::-1]:
    print('descending')
else:
    print('mixed')