from collections import Counter
def solution(topping):    
    answer = 0
    chulsu = Counter(topping)
    bro = set()
    for i in topping:
        chulsu[i] -= 1
        if chulsu[i] == 0:
            chulsu.pop(i)
        bro.add(i)
        if len(chulsu) == len(bro):
            answer += 1
    return answer