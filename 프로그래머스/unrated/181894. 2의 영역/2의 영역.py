def solution(arr):
    answer = []
    if 2 not in arr:
        return [-1]
    a = arr.index(2)
    arr1 = arr[::-1]
    b = arr1.index(2)
    return arr[a:len(arr)-b]