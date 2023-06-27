def solution(strArr):
    arr = [0] * 31
    for i in range(len(strArr)):
        arr[len(strArr[i])] += 1
    return max(arr)