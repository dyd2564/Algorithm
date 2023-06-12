def solution(arr):
    answer = 1
    
    def GCD(a, b):
        while b:
            a, b = b, a%b
        return a
    
    for i in arr:
        answer *= i // GCD(answer, i)
        
    
    return answer