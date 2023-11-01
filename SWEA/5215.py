def dfs(index, score, calories):
    global answer
    if calories > L:
        return
    if index >= N:
        if score > answer:
            answer = score
        return

    dfs(index + 1, score + ingredients[index][0], calories + ingredients[index][1])
    dfs(index + 1, score, calories)


T = int(input())

for test_case in range(1, T + 1):
    N, L = map(int, input().split())
    ingredients = []
    for _ in range(N):
        ingredients.append(list(map(int, input().split())))
    answer = 0
    dfs(0, 0, 0)
    print("#%d %d" % (test_case, answer))
