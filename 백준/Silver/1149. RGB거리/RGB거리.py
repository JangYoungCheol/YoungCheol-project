# 집은 빨강, 초록, 파랑 중 하나의 색으로 칠한다.
# 최소 비용

#1번 집의 색은 2번 집의 색과 같지 않아야한다
#N번 집의 색은 N-1번의 집의 색과 같지 않아야한다
#i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.


N = int(input())
# matrix[i][0]: 빨강, [1]: 초록, [2]: 파랑
matrix = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    # i번째 집을 빨강(0)으로 칠할 때 최소 비용
    matrix[i][0] += min(matrix[i - 1][1], matrix[i - 1][2])

    # i번째 집을 초록(1)으로 칠할 때 최소 비용
    matrix[i][1] += min(matrix[i - 1][0], matrix[i - 1][2])

    # i번째 집을 파랑(2)으로 칠할 때 최소 비용
    matrix[i][2] += min(matrix[i - 1][0], matrix[i - 1][1])

# 마지막 집(N-1)의 빨강, 초록, 파랑 누적 비용 중 가장 작은 값 출력
print(min(matrix[N - 1]))