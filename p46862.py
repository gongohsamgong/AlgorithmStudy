def solution(n, lost, reserve):
    answer = 0
    result = [0] * (n+2)

    for i in range(1, n+1):
        if i not in lost:
            result[i] = 1

    for i in range(len(reserve)):
        if reserve[i] in lost:
            result[reserve[i]] = 1
        else:
            result[reserve[i]] = 2

    for i in range(1, n+1):
        if result[i] == 0:
            if result[i-1] == 2:
                result[i-1] = result[i] = 1
            elif result[i+1] == 2:
                result[i+1] = result[i] = 1

    for i in range(1, n+1):
        if result[i] > 0:
            answer += 1

    return answer
#
# def solution(n, lost, reserve):
#     answer = 0
#     result = [1] * (n+2)
#
#     for l in lost:
#         result[l] -= 1
#     for r in reserve:
#         result[r] += 1
#
#     for i in range(1, n+1):
#         if result[i] == 0:
#             if result[i-1] == 2:
#                 result[i-1] = result[i] = 1
#             elif result[i+1] == 2:
#                 result[i+1] = result[i] = 1
#
#     for i in range(1, n+1):
#         if result[i] > 0:
#             answer += 1
#
#     return answer