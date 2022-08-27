N, M, K = map(int, input().split())
cnt = 0
cnt2 = 0
sum_ = 0

arr = list(map(int, input().split()))
arr.sort(reverse=True)

if arr[0] != arr[1]:    # 다른 max값
    while cnt < M:
        while cnt2 < K:
            sum_ += arr[0]
            cnt2 += 1
            cnt += 1
            print(sum_)
        cnt2 = 0
        sum_ += arr[1]
        cnt += 1
        print(sum_)

print(sum_)