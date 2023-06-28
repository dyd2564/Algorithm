def solution(my_string):
    answer = []
    arr1 = [0] * 26
    arr2 = [0] * 26
    for i in my_string:
        if i == i.upper():
            arr1[ord(i)-65] += 1
        else:
            arr2[ord(i)-97] += 1
    return arr1+arr2