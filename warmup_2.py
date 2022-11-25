def solution(array):
    answer = 0
    temp = ''
    for i in range(len(array)):
        temp += str(array[i])
    for i in range(len(temp)):
        if '7' == temp[i]:
            answer += 1
    return answer
