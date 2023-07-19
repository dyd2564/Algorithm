def solution(players, callings):
    answer = []
    arr = [i for i in range(len(players))]
    # print(arr)
    
    for i in callings:
        arr[players.index(i)] -= 1
        arr[players.index(i)-1] += 1
        print(arr)
    
    
    return players