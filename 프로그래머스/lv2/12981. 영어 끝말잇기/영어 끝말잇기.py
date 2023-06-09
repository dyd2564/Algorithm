def solution(n, words):
    answer = [0, 0]
    arr = [words[0]]
    for i in range(1, len(words)):        
        if arr[-1][-1] == words[i][0] and words[i] not in arr:
            arr.append(words[i])
        else:
            answer[0] = (i % n) + 1
            answer[1] = (i // n) + 1
            break
    
    return answer