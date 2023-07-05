def solution(rank, attendance):
    attend = 0
    arr = []
    ranking = 1
    while attend < 3:
        if attendance[rank.index(ranking)]:
            arr.append(rank.index(ranking))
            attend += 1
        ranking += 1
    
    return arr[0] * 10000 + arr[1] * 100 + arr[2]