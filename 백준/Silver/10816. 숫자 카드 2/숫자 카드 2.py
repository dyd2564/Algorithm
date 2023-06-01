import sys
from collections import Counter
input = sys.stdin.readline
n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

c = Counter(arr1)

for i in range(len(arr2)):
    if arr2[i] in c:
        print(c[arr2[i]], end=' ')
    else:
        print(0, end=' ')

