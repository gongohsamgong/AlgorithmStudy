def solution(my_string):
    answer = ''
    _string = my_string.lower()
    answer = answer.join(sorted(_string))
    return answer