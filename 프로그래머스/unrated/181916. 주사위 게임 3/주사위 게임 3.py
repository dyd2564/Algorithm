from collections import Counter
def solution(a, b, c, d):
    arr = [a, b, c, d]
    cnt_arr = [arr.count(i) for i in arr]
    print(cnt_arr)
    if max(cnt_arr) == 4:
        return 1111*a
    
    elif max(cnt_arr) == 3:
        p = arr[cnt_arr.index(3)]
        q = arr[cnt_arr.index(1)]
        return (10 * p + q)**2
    
    elif max(cnt_arr) == 2:
        if min(cnt_arr) == 2:
            return (a + c) * abs(a - c) if a == b else (a + b) * abs(a - b)
        else:
            p = arr[cnt_arr.index(2)]
            return (a*b*c*d) / p**2
    else:
        return min(arr)
        
        
        
