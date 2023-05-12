import sys


if __name__ == "__main__":
    read = sys.stdin.readline
    N, K = map(int, read().split())
    A = list(map(int, read().split()))
    B = list(map(int, read().split()))
    A.sort()
    B.sort(reverse=True)
    for i in range(K):
        if A[i] < B[i]:
            A[i], B[i] = B[i], A[i]
        # 이미 정렬된 상태이니 이후로 B 배열로 바꿔줄 필요가 없으므로 그냥 break
        else:
            break
    print(sum(A))
