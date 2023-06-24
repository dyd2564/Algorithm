def solution(myStr):
    answer = []
    myStr = myStr.replace('a', '-').replace('b', '-').replace('c', '-')
    myStr = myStr.split('-')
    for i in myStr:
        if i:
            answer.append(i)
    if len(answer) == 0:
        answer.append("EMPTY")
    return answer