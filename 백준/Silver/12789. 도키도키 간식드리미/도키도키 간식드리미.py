import sys

n = int(sys.stdin.readline())
line = list(map(int, sys.stdin.readline().split()))

stack = []
target = 1

# 알고리즘 실행
for student in line:
    stack.append(student) 
    
    # 추가 공간의 맨 앞이 현재 받아야 할 순번과 일치하면 간식 배부
    while stack and stack[-1] == target:
        stack.pop()
        target += 1

# 출력
if not stack:
    print("Nice")
else:
    print("Sad")