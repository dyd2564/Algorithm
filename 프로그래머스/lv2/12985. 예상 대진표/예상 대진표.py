import math
def solution(n,a,b):
    answer = 1

    while True:
        if min(a, b) % 2 == 1 and min(a, b) + 1 == max(a, b):
            break 
        # 1 2 3 4(A) 5 6 7 8 9 10 11 12 13 14 15(B) 16
        # 1 2(A) 3 4 5 6 7 8(B)
        # 1(A) 2 3 4(B)
        # 1(A) 2(B)
        # n = n // 2
        a = math.ceil(a/2)
        b = math.ceil(b/2)
        answer += 1
                   
    return answer