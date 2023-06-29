def solution(arr):
    a = 0
    while True:
        cnt = 0
        a += 1
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                arr[i] //= 2
                cnt += 1
                # arr2.append(arr[i]//2)
            elif arr[i] < 50 and arr[i] % 2 == 1:
                arr[i] = arr[i]*2+1
                cnt += 1
                # arr2.append(arr[i]*2+1)
        
        if cnt == 0:
            break                
    return a-1