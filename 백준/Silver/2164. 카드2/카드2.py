import sys

input = sys.stdin.readline
from collections import deque

q = deque()
n = int(input())

for i in range(1, n + 1):
    q.append(i)

while True:
    if len(q) > 1:
        q.popleft()
    else:
        break
    a = q.popleft()
    q.append(a)
print(q[0])

