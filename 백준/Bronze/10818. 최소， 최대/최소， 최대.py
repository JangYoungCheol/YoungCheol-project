
N = int(input())

lst = list(map(int, input().split()))

max_lst = lst[0]
min_lst = lst[0]
for i in range(N):
    if lst[i] > max_lst:
        max_lst = lst[i]

    if lst[i] < min_lst:
        min_lst = lst[i]


print(f'{min_lst} {max_lst}')