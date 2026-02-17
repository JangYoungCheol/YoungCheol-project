matrix = [list(map(int, input().split())) for _ in range(9)]


max_matrix = -1
a = 0
b = 0
for i in range(9):
    for j in range(9):
        if max_matrix < matrix[i][j]:
            max_matrix = matrix[i][j]
            a, b = i+1 , j+1

print(max_matrix)
print(a, b)