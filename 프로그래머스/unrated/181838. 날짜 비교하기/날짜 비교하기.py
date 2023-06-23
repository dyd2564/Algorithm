def solution(date1, date2):
    d1 = str(date1[0]) + str(date1[1]) + str(date1[2]) 
    d2 = str(date2[0]) + str(date2[1]) + str(date2[2])
    if int(d2) - int(d1) > 0:
        return 1
    return 0