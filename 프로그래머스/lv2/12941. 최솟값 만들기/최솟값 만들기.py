def solution(A,B):
    answer = 0
    a = len(A)
    A.sort()
    B.sort(reverse=True)
    if len(A) < len(B):
        a = len(B)
    for i in range(a):
        answer += A[i]*B[i]

    return answer