def dfs(index, count):
    global answer
    if count == int(cnt):
        answer = max(int(''.join(numbers)), answer)
        return
    for now in range(index, len(numbers)):
        for max_idx in range(now + 1, len(numbers)):
            if numbers[now] <= numbers[max_idx]:
                numbers[now], numbers[max_idx] = numbers[max_idx], numbers[now]
                dfs(now, count + 1)
                numbers[now], numbers[max_idx] = numbers[max_idx], numbers[now]
    if answer == 0 and count < int(cnt):
        extra = (int(cnt) - count) % 2
        if extra == 1:
            numbers[-1], numbers[-2] = numbers[-2], numbers[-1]
        dfs(index, int(cnt))


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    temp, cnt = input().split()
    numbers = list(temp)
    answer = 0
    dfs(0, 0)
    print("#%d %d" % (test_case, answer))
