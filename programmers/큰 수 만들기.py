"""
import itertools

def solution(number, k):
    answer = 0
    combination_list = list(itertools.combinations(number, len(number) - k))
    print(combination_list)
    for i in range(len(combination_list)):
        num = ""
        for j in range(len(number) - k):
            num += combination_list[i][j]
        answer = max(int(num), int(answer))
    return str(answer)
"""


def solution(number, k):
    stack = []
    for num in number:
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)
    return ''.join(stack)


number = "1231234"
k = 3
print(solution(number, k))
