import sys

def cut(array, start, end, n):
    while start <= end:
        mid = (start + end) // 2
        num = 0
        for i in range(len(array)):
            if mid != 0:
                num += array[i] // mid
            else:   # mid == 0일 경우 나누기 불가. 따라서 1을 더해준 예외를 만들어줄 것
                num += array[i] // (mid + 1)
        if num < n:
            end = mid - 1
        else:
            start = mid + 1
    return end


if __name__ == '__main__':
    read = sys.stdin.readline
    k, n = map(int, read().split())
    array = []
    for i in range(k):
        array.append(int(read()))
    print(cut(array, 0, max(array), n)) # 참고록 start = 0 대신 start = min(arr)를 하면 당연히 안되는것을 알것이다. 멍청아.