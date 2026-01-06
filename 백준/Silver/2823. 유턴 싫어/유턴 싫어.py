import sys

def solve():
    # 1. 입력 받기
    # R: 행의 개수, C: 열의 개수
    try:
        line1 = sys.stdin.readline().split()
        if not line1:
            return
        R, C = map(int, line1)
        
        # 지도 정보 입력
        grid = [list(sys.stdin.readline().strip()) for _ in range(R)]
    except ValueError:
        return

    # 상, 하, 좌, 우 이동을 위한 델타값
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    has_dead_end = False

    # 2. 모든 칸을 순회하며 검사
    for x in range(R):
        for y in range(C):
            # 현재 위치가 길('.')인 경우에만 검사
            if grid[x][y] == '.':
                connected_roads = 0
                
                # 4방향 탐색
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    
                    # 지도 범위를 벗어나지 않고, 이웃한 칸이 길('.')인 경우
                    if 0 <= nx < R and 0 <= ny < C:
                        if grid[nx][ny] == '.':
                            connected_roads += 1
                
                # 연결된 길이 2개 미만이면(1개이거나 0개), 들어왔다가 유턴해야만 나갈 수 있음
                if connected_roads < 2:
                    has_dead_end = True
                    break # 하나라도 막다른 길이 있으면 더 볼 필요 없음
        
        if has_dead_end:
            break

    # 3. 결과 출력
    # 막다른 길이 있으면(상근이가 싫어함) -> 1 (Bad)
    # 막다른 길이 없으면(상근이가 좋아함) -> 0 (Good)
    if has_dead_end:
        print(1) 
    else:
        print(0)

if __name__ == "__main__":
    solve()