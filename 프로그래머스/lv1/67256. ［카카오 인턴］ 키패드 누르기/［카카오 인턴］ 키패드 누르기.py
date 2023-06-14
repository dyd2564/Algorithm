def solution(numbers, hand):
    answer = ''
    left, right = 10, 12
    
    for i in numbers:
        if i in [1, 4, 7]:
            answer += 'L'
            left = i
        elif i in [3, 6, 9]:
            answer += 'R'
            right = i
        else:
            if i == 0:
                i = 11
            left_num = abs(i - left)
            right_num = abs(i - right)
            left_dis = left_num // 3 + left_num % 3
            right_dis = right_num // 3 + right_num % 3
            if left_dis > right_dis:
                right = i
                answer += 'R'
            elif left_dis < right_dis:
                left = i
                answer += 'L'
            else:
                if hand == "right":
                    right = i
                    answer += 'R'
                else:
                    left = i
                    answer += 'L'
                
            
            
    return answer