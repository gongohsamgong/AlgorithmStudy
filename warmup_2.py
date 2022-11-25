def solution(array):
    answer = 0
    for i in range(len(array)):
        if '7' in str(array[i]):
            for j in range(len(str(array[i]))):
                if '7' == str(array[i])[j]:
                    answer += 1
    return answer