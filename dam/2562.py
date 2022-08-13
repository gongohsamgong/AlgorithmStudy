arr = []

for i in range(9):
    n = int(input())
    arr.append(n)

maximum = max(arr)

for i in range(9):
    if arr[i] == maximum:
        print(maximum)
        print(i+1)