import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    
    queue = deque([(0, 0)])
    visited[0][0] = True
    
    while queue:
        x, y = queue.popleft()
        
        # 끝 점에 도달한 경우 (승리)
        if x == N - 1 and y == N - 1:
            return "HaruHaru"
        
        jump = board[x][y]
        
        # 점프 거리가 0인 경우 무한 루프 방지
        if jump == 0:
            continue
            
        # 아래로 이동
        nx, ny = x + jump, y
        if nx < N and ny < N and not visited[nx][ny]:
            visited[nx][ny] = True
            queue.append((nx, ny))
            
        # 오른쪽으로 이동
        nx, ny = x, y + jump
        if nx < N and ny < N and not visited[nx][ny]:
            visited[nx][ny] = True
            queue.append((nx, ny))
            
    # 큐가 빌 때까지 도달하지 못한 경우 (패배)
    return "Hing"

print(solve())