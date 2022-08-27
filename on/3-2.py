N, M, K = map(int, input().split())
cnt = 0
cnt2 = 0
sum_ = 0

arr = list(map(int, input().split()))
arr.sort(reverse=True)
print(arr)

if arr[0] != arr[1]:    # 다른 max값
    while cnt < M:
        while cnt2 < K: # 이 부분 때문에 else문 꼭 필요. 아님 k번 더 더하게 됨.
            sum_ += arr[0]
            cnt2 += 1
            cnt += 1
        cnt2 = 0
        sum_ += arr[1]
        cnt += 1

else:
    sum_ = arr[0] * M

print(sum_)