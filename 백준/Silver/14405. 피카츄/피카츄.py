# 문자열 S가 주어질때 피카츄가 발음할 수 있는 문자열인지 구해보셔
s = input().strip()

for word in ["pi", "ka", "chu"]:
    s = s.replace(word, " ")
    
if not s.strip():
    print("YES")
else:
    print("NO")