# 심장의 위치는 머리 바로 밑에 칸
# 허리는 심장 바로 아래쪽에 붙어 있다.

# 출력은 심장의 위치
# 팔, 다리 ,허리의 길이를 구하기

# 제일 첫번째 칸은 1,1

# * 쿠키 신체 부분
# _ 아무 것도 아닌 부분

N = int(input())
matrix = [list(input().strip()) for _ in range(N)]

# 일단 머리 위치부터 찾기 머리가 제일 위에 존재하다보니 머리를 찾고
# 행크기만 1 늘려주면 심장 위치 찾기 가능

hr, hc = 1, 1
visited = 0

for i in range(N):
    for j in range(N):
        if matrix[i][j] == '*':
            hr = i + 1
            hc = j
            visited = 1
            break
    if visited:
        break
print(hr+1, hc+1)

# 왼쪽 팔 구하기
left_arm = 0
lc = hc - 1
while lc >= 0 and matrix[hr][lc] == '*':
    left_arm += 1
    lc -= 1

# 오른쪽 팔 길이 구하기
right_arm = 0
rc = hc + 1
while rc <N and matrix[hr][rc] == '*':
    right_arm += 1
    rc += 1

# 허리길이 구하기
wasit = 0
w = hr + 1
while w < N and matrix[w][hc] == '*':
    wasit += 1
    w += 1

# 왼쪽 다리 길이 구하기
left_leg = 0
ll = w 
while ll < N and matrix[ll][hc - 1] == '*':
    left_leg += 1
    ll += 1
# 오른쪽 다리 길이 구하기

right_leg = 0
rl = w 
while rl < N and matrix[rl][hc + 1] == '*':
    right_leg += 1
    rl += 1


print(f'{left_arm} {right_arm} {wasit} {left_leg} {right_leg}')
