def solution(N, name, kor, eng):
    answer = []
    arr = [(name[i], kor[i], eng[i]) for i in range(N)]
    arr.sort(key=lambda x: (x[1], -x[2], x[0]))

    for n in arr:
        answer.append(n[0])

    return answer
