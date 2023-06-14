def solution(N, stages):
    answer = []
    dic = {}
    user = len(stages)
    for i in range(1, N+1):
        a = stages.count(i)
        if a == 0:
            dic[i] = 0
        else:
            dic[i] = a / user
            user -= a
    dic = dict(sorted(dic.items(), key=lambda x:x[1], reverse=True))
    answer = list(dic.keys())
            
            
            
            
        
            
            
    return answer