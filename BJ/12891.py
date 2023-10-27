import sys

read = sys.stdin.readline
S, P = map(int, read().split())
dna = list(read().rstrip())
check, answer = 0, 0
choices = ['A', 'C', 'G', 'T']

# 0: A, 1: C, 2: G, 3: T
temp = list(map(int, read().split()))
check_dict = {'A': temp[0], 'C': temp[1], 'G': temp[2], 'T': temp[3]}
for base in choices:
    if check_dict[base] == 0:
        check += 1

my_array = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

# 첫번째 dna 조합
for i in range(P):
    my_array[dna[i]] += 1
    if check_dict[dna[i]] == my_array[dna[i]]:
        check += 1

if check == 4:
    answer += 1

# 슬라이딩 윈도우
for i in range(P, S):
    j = i - P
    my_array[dna[i]] += 1
    if check_dict[dna[i]] == my_array[dna[i]]:
        check += 1
    if check_dict[dna[j]] == my_array[dna[j]]:
        check -= 1
    my_array[dna[j]] -= 1
    if check == 4:
        answer += 1

print(answer)
