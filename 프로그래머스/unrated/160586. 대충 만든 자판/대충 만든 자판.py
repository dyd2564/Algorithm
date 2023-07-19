def solution(keymap, targets):
    answer = []
    
    for i in targets: #ABCD
        # print(i, "----")
        a = 0
        for j in range(len(i)):
            # print(i[j], '-')
            arr = []
            for k in keymap:
                
                if i[j] in k:
                    arr.append(k.find(i[j]))
                # print(arr)
                # else:
                #     a = 0
                #     break
            arr1 = set(arr)
            if arr1 and -1 not in arr1:
                a += min(arr1)+1
            else:
                a = 0
                break
            # else:
                # a = 0
        if a == 0:
            answer.append(-1)
        else:
            answer.append(a)
        # print(a)
            # if arr1:
            #     answer.append(min(arr1)+1)
            # else:
            #     answer.append(-1)
    return answer