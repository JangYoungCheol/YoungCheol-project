import sys

def solve():
    # 입력 처리
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    M, N, K = map(int, data[:3])
    
    # M x N 모눈종이 초기화 (0: 빈 영역, 1: 직사각형 영역)
    grid = [[0] * N for _ in range(M)]
    
    # 직사각형 영역 칠하기
    idx = 3
    for _ in range(K):
        x1, y1, x2, y2 = map(int, data[idx:idx+4])
        idx += 4
        for y in range(y1, y2):
            for x in range(x1, x2):
                grid[y][x] = 1
                
    # 방향 벡터 (상, 하, 좌, 우)
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    
    areas = []
    
    # 모든 좌표를 탐색하며 빈 영역(0) 찾기
    for i in range(M):
        for j in range(N):
            if grid[i][j] == 0:
                # DFS를 위한 스택 초기화
                stack = [(i, j)]
                grid[i][j] = 1 # 방문 처리
                area = 0
                
                # DFS 탐색 진행
                while stack:
                    cy, cx = stack.pop()
                    area += 1
                    
                    for d in range(4):
                        ny = cy + dy[d]
                        nx = cx + dx[d]
                        
                        if 0 <= ny < M and 0 <= nx < N and grid[ny][nx] == 0:
                            grid[ny][nx] = 1
                            stack.append((ny, nx))
                            
                areas.append(area)
                
    # 넓이를 오름차순으로 정렬
    areas.sort()
    
    # 결과 출력
    print(len(areas))
    print(*(areas))

if __name__ == '__main__':
    solve()