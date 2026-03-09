# 1 X 1 X 1  크기의 블록


# 세로 N 가로 M 집터
# 집터 내의 땅 높이를 똑같이 만들기
# B는 인벤토리 있는 블록개수
N, M, B = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]

# 1. 좌표(i, j)의 가장 위에 있는 블록을 제거하여 인벤토리에 넣는다

# 2. 인벤토리에서 블록 하나를 꺼내어 좌표 (i, j)의 가장 위에 있는 블록 위에 놓는다.

# 1번작업은 2초 2번작업은 1초 소요

cnt = float('inf')  # 최소 시간을 저장할 변수로 사용
ans_h = 0           # 정답 높이 저장

# 가능한 모든 땅의 높이(0~256)를 탐색
for h in range(257):
    remove = 0
    add = 0
    
    for i in range(N):
        for j in range(M):
            diff = matrix[i][j] - h
            if diff > 0:
                remove += diff  # 목표 높이보다 높으면 블록 제거
            else:
                add -= diff     # 목표 높이보다 낮으면 블록 추가
                
    # 인벤토리의 블록(B)과 제거한 블록(remove)으로 추가(add)를 감당할 수 있는지 확인
    if remove + B >= add:
        time = (remove * 2) + add
        
        # 최소 시간(cnt) 갱신 (시간이 같으면 더 높은 높이 선택)
        if time <= cnt:
            cnt = time
            ans_h = h

print(cnt, ans_h)