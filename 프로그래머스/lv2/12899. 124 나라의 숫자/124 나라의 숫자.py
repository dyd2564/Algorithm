def solution(n):
    answer = ''
    num = ["4", "1", "2"]

    
    while n >= 1:
        if n % 3 != 0:
            answer += num[n % 3]
            n //= 3
        else:
            answer += "4"
            n = n//3 - 1
    return answer[::-1]