def solution(myString, pat):
    answer = ''
    # myString = myString[::-1]
    # pat = pat[::-1]
    # if pat in myString:
    a = []
    a.append(myString[::-1].find(pat[::-1]))
    b = (myString[::-1].find(pat[::-1]))
    if b == 0:
        return myString
    return myString[:-b]