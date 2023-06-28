def solution(ineq, eq, n, m):
    a = ineq + eq
    if a == '>=':
        if n >= m:
            return 1
    elif a == '<=':
        if n <= m:
            return 1
    elif a == '>!':
        if n > m:
            return 1
    else:
        if n < m: 
            return 1    
    return 0