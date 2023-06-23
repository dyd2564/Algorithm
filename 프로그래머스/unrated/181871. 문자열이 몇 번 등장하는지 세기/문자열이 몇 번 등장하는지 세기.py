def solution(myString, pat):
    cnt = 0
    a = 0
    for i in range(a, len(myString)-len(pat)+1):
        if myString[i:i+len(pat)] == pat:
            cnt += 1
    return cnt