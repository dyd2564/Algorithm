def solution(s):
    answer = []
    cnt, cnt_zero = 0, 0
    while True:
        if s == '1':
            break
        else:
            cnt_zero += s.count('0')
            s = s.replace('0', '')
            s = bin(len(s))[2:]
        cnt += 1
    answer.append(cnt)
    answer.append(cnt_zero)
    return answer