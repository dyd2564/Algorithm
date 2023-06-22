def solution(arr1, arr2):
    a, b = len(arr1), len(arr2)
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        if sum(arr1) > sum(arr2):
            return 1
        elif sum(arr1) < sum(arr2):
            return -1
        else:
            return 0
