import sys

# 방 번호 입력
room_number = sys.stdin.readline().strip()
counts = [0] * 10

# 각 숫자의 빈도수 계산
for num in room_number:
    if num == '6' or num == '9':
        counts[6] += 1
    else:
        counts[int(num)] += 1

# 6과 9의 필요 세트 수 계산 (올림)
counts[6] = (counts[6] + 1) // 2

# 배열 중 최댓값이 필요한 세트의 최솟값
print(max(counts))