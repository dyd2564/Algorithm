def solution(players, callings):
    answer = []
    play = {rank : i for i, rank in enumerate(players)}
    # print(play)
    for i in callings:
        idx = play[i]
        
        play[i] -= 1
        play[players[idx-1]] += 1
        
        players[idx-1], players[idx] = players[idx], players[idx-1]
        
    return players