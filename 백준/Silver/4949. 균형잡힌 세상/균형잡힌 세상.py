import sys

def solve():
    while True:
        line = sys.stdin.readline().rstrip('\n')
        
        # 입력의 종료 조건: 온점 하나만 들어온 경우
        if line == ".":
            break
            
        stack = []
        is_balanced = True
        
        for char in line:
            if char == '(' or char == '[':
                stack.append(char)
            elif char == ')':
                if not stack or stack[-1] != '(':
                    is_balanced = False
                    break
                stack.pop()
            elif char == ']':
                if not stack or stack[-1] != '[':
                    is_balanced = False
                    break
                stack.pop()
        
        # 모든 검사 후 스택이 비어있어야 함
        if is_balanced and not stack:
            print("yes")
        else:
            print("no")

solve()