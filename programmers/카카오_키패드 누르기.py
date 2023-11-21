def solution(numbers, hand):
    answer = ''
    pad = {1: (0, 0), 2: (0, 1), 3: (0, 2),
           4: (1, 0), 5: (1, 1), 6: (1, 2),
           7: (2, 0), 8: (2, 1), 9: (2, 2),
           '*': (3, 0), 0: (3, 1), '#': (3, 2)}
    left_location = pad['*']
    right_location = pad['#']
    for num in numbers:
        if num == 1 or num == 4 or num == 7:
            answer += 'L'
            left_location = pad[num]
        elif num == 3 or num == 6 or num == 9:
            answer += 'R'
            right_location = pad[num]
        else:
            target_x, target_y = pad[num]
            left_x, left_y = left_location
            right_x, right_y = right_location
            l_distance = abs(left_x - target_x) + abs(left_y - target_y)
            r_distance = abs(right_x - target_x) + abs(right_y - target_y)
            if l_distance < r_distance:
                left_location = pad[num]
                answer += 'L'
            elif l_distance > r_distance:
                right_location = pad[num]
                answer += 'R'
            else:
                if hand == "left":
                    left_location = pad[num]
                    answer += 'L'
                else:
                    right_location = pad[num]
                    answer += 'R'
    return answer


numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"
print(solution(numbers, hand))
