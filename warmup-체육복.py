def solution(n, lost, reserve):
    answer = 0
    clothes = [1] * (n + 2)
    for i in lost:
        clothes[i] -= 1
    for j in reserve:
        clothes[j] += 1

    for i in range(n + 1):
        if clothes[i]:
            continue
        if clothes[i - 1] == 2:
            clothes[i - 1] -= 1
            clothes[i] += 1
        elif clothes[i + 1] == 2:
            clothes[i + 1] -= 1
            clothes[i] += 1

    for i in range(1, n + 1):
        if clothes[i]:
            answer += 1

    return answer