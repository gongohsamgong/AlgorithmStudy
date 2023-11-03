def dfs(index, total):
    global answer
    if total == K:
        answer += 1
        return
    if total > K:
        return
    for i in range(index, N):
        dfs(i+1, total + A[i])


T = int(input())
for test_case in range(1, T + 1):
    answer = 0
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    dfs(0, 0)
    print("#%d %d" % (test_case, answer))
