# 계수 정렬을 이용한 풀이

# N(가게의 부품 개수)입력받기
n = int(input())
array = [0] * 1000001

# 가게에 있는 전체 부품 번호를 입력받아서 기록
for i in input().split():
    array[int(i)] = 1

# M(손님이 확인 요청한 부품 개수)을 입력받기
m = int(input())

# 손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
request = list(map(int, input().split()))

# 손님이 확인 요청한 부품번호를 하나씩 확인
for i in request:
    # 해당 부품이 존재하는지 확인
    if array[i]==1:
        print('yes', end=' ')
    else:
        print('no', end=' ')