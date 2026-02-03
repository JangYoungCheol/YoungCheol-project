N, X = map(int, input().split())
lst = list(map(int, input().split()))

# 1. 초기 X일 간의 합 구하기
current_sum = sum(lst[:X])
max_sum = current_sum
count = 1

# 2. 슬라이딩 윈도우: 한 칸씩 이동하며 합 갱신
for i in range(X, N):
    # 새로운 값 더하고, 맨 앞의 값 빼기
    current_sum += lst[i]
    current_sum -= lst[i - X]

    # 최대값 갱신 및 개수 세기
    if current_sum > max_sum:
        max_sum = current_sum
        count = 1  # 새로운 최대값이 나오면 개수 초기화
    elif current_sum == max_sum:
        count += 1  # 같은 최대값이면 개수 추가

# 3. 결과 출력
if max_sum == 0:
    print("SAD")
else:
    print(max_sum)
    print(count)
