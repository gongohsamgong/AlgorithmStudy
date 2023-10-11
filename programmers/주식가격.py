"""
def solution(prices):
    length = len(prices)
    answer = [0] * length
    for i in range(length):
        for j in range(i+1, length):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer
"""


def solution(prices):
    stack = []
    answer = [0] * len(prices)
    for i in range(len(prices)):
        # 감소했을 때
        while stack != [] and stack[-1][1] > prices[i]:
            past, _ = stack.pop()
            answer[past] = i - past
        stack.append([i, prices[i]])
    for i, s in stack:
        answer[i] = len(prices) - 1 - i
    return answer
