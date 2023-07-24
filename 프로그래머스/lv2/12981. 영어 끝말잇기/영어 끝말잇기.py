def solution(n, words):
    answer = []
    word = [words[0]]
    for i in range(1, len(words)):
        if word[-1][-1] == words[i][0] and words[i] not in word:
            word.append(words[i])
        else:
            return [(i%n)+1, (i//n)+1]
    

    return [0, 0]