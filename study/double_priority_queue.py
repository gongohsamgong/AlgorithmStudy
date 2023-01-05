def solution(operations):
    answer = []
    temp = []

    for val in operations:
        instruction, number = val.split(' ')
        if instruction == "I":
            temp.append(int(number))
        else:
            if len(temp) > 0:
                if int(number) == 1:
                    temp.pop()
                elif number == '-1':
                    temp.pop(0)
            else:
                continue
        temp.sort()

    if len(temp) == 0:
        answer = [0, 0]
    else:
        answer.append(max(temp))
        answer.append(min(temp))
    return answer
