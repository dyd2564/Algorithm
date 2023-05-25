N, M = map(int, input().split())
result = []
chess = []
for _ in range(N):
    chess.append(input())
for i in range(N-7):
    for j in range(M-7):
        chess1 = 0
        chess2 = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0:
                    if chess[a][b] == 'B':
                        chess1 += 1
                    else:
                        chess2 += 1
                else:
                    if chess[a][b] == 'W':
                        chess1 += 1
                    else:
                        chess2 += 1
        result.append(chess1)
        result.append(chess2)
print(min(result))
                
                
                