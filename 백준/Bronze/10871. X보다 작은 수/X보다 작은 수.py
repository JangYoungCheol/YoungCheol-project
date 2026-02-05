N, X = map(int, input().split())

lst = list(map(int, input().split()))

lst1 = []

for i in lst:
    if i < X:
        lst1.append(i)

print(*lst1)