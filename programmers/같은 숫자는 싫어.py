"""
def solution(arr):
    answer = []
    for i in range(len(arr)):
        target = arr[i]
        if i == 0:
            answer.append(target)
            continue
        if arr[i-1] == target:
            continue
        answer.append(target)
    return answer
"""


def solution(arr):
    answer = []
    for n in arr:
        if answer[-1:] == [n]:
            continue
        answer.append(n)
    return answer


arr = [1, 1, 3, 3, 0, 1, 1]
print(solution(arr))
