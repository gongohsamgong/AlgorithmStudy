clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

def solution(clothes):
    answer = 1
    fashion_dict = {}
    for cloth, type in clothes:
        if type in fashion_dict:
            fashion_dict[type] += 1
        else:
            fashion_dict[type] = 1
    for type in fashion_dict:
        answer *= (fashion_dict[type] + 1)
    return answer - 1

print(solution(clothes))