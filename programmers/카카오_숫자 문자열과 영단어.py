"""
def solution(s):
    answer, word = '', ''
    int_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    str_numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(len(s)):
        word += s[i]
        if word in int_numbers:
            answer += word
            word = ''
        elif word in str_numbers:
            word = int_numbers[str_numbers.index(word)]
            answer += word
            word = ''
    return int(answer)
"""


def solution(s):
    answer = 0
    str_numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(10):
        s = s.replace(str_numbers[i], str(i))
    answer = int(s)
    return answer


s = "one4seveneight"
print(solution(s))
