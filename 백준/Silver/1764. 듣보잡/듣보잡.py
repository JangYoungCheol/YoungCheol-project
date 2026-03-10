import sys

# 입력 데이터 전체 읽기 (입출력 속도 최적화)
input_data = sys.stdin.read().split()

if len(input_data) >= 2:
    n = int(input_data[0])
    m = int(input_data[1])

    # 듣도 못한 사람 집합(Set) 구성
    unheard = set(input_data[2:n+2])
    # 보도 못한 사람 집합(Set) 구성
    unseen = set(input_data[n+2:])

    # 교집합 구하기 및 사전순 정렬
    result = sorted(list(unheard & unseen))

    # 결과 출력
    print(len(result))
    if result:
        print('\n'.join(result))