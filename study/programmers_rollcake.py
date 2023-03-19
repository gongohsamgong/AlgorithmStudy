topping = [1, 2, 1, 3, 1, 4, 1, 2]

def findUnique(topping):
    unique = []
    for i in range(len(topping)):
        if topping[i] not in unique:
            unique.append(topping[i])
    return unique

def solution(topping):
    answer = 0
    uniqueTopping = findUnique(topping)
    if len(uniqueTopping) % 2 != 0:
        return answer
    for i in range(1, len(topping)):
        # 나누는 부분만 잘 설정하면 되는데..... 시간초과
        topping1 = topping[0:i]
        topping2 = topping[i:]
        if findUnique(topping1) == findUnique(topping2):
            answer + 1
    return answer

print(solution(topping))