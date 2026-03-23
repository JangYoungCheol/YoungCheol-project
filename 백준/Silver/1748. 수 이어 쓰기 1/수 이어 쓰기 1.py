N = int(input())

ans = 0     # 총 자릿수
length = 1  # 현재 계산 중인 자릿수 길이 (1, 2, 3...)
start = 1   # 현재 자릿수의 시작 숫자 (1, 10, 100...)

while start <= N:
    # 현재 자릿수의 마지막 숫자 (예: 1자리수면 9, 2자리수면 99)
    # N이 그보다 작다면 N까지만 계산
    end = min(N, start * 10 - 1)
    
    # (끝 숫자 - 시작 숫자 + 1) × 현재 자릿수 길이를 더함
    ans += (end - start + 1) * length
    
    # 다음 자릿수로 이동
    length += 1
    start *= 10

print(ans)