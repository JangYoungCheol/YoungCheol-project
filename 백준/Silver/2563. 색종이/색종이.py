# 가로 세로의 크기가 각각 100

paper = [[0]*100 for _ in range(100)]
# 색종이 수
N = int(input())

cnt = 0
for _ in range(N):
    x, y = map(int, input().split())


    for i in range(x, x + 10):
        for j in range(y, y+10):
            if paper[i][j] == 0:
                paper[i][j] = 1
                cnt +=1

print(cnt)



# 전체 도화지를 1칸 1칸씩으로 해서 채워보자
# 이미 있으면 패스

