def solution(arr, queries):
    answer = []
    for i in queries:
        a = arr[i[0]:i[1]+1]
        a.sort()
        if max(a) <= i[2]:
            answer.append(-1)
        else:    
            for j in a:
                if j > i[2]:
                    answer.append(j)
                    break
        
            
        
    return answer