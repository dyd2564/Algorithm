import sys

input = sys.stdin.readline
from collections import deque

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    q = deque(list(map(int, input().split())))
    cnt = 0
    while q:
        max_q = max(q)
        a = q.popleft()
        m -= 1

        if a == max_q:
            cnt += 1
            if m < 0:
                print(cnt)
                break
        else:
            q.append(a)
            if m < 0:
                m = len(q) - 1