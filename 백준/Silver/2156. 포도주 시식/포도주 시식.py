import sys

# 입력 속도 향상을 위해 sys.stdin.read 사용
input_data = sys.stdin.read().split()

if not input_data:
    exit()

n = int(input_data[0])
wine = [0] * 10001
dp = [0] * 10001

for i in range(1, n + 1):
    wine[i] = int(input_data[i])

# 초기값 설정
dp[1] = wine[1]
if n >= 2:
    dp[2] = wine[1] + wine[2]

# 동적 계획법 수행
for i in range(3, n + 1):
    dp[i] = max(dp[i-1], dp[i-2] + wine[i], dp[i-3] + wine[i-1] + wine[i])

# 결과 출력
print(dp[n])