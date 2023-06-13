def solution(elements):
    arr = []
    a = elements*2
    for i in range(len(elements)):
        for j in range(len(elements)):
            arr.append(sum(a[i:i+j]))
    return len(set(arr))