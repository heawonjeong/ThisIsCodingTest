# 이진 탐색 소스코드 구현(반복문)
def binary_search(array, target,start, end):
    while start <= end:
        mid = (start + end)//2
    if array[mid]==target:
        return mid
    
    # 중간점의 값보다 찾고자 하는 값이 작을 경우 왼쪽 탐색
    elif array[mid] > target:
        end = mid -1
    
    # 중간점의 값보다 찾고자 하는 값이 클 경우 오른쪽 탐색\
    else:
        start = mid + 1

    return None

# N(가게의 부품 개수)입력
n = int(input())
# 가게에 있는 전체 부품 번호를 공백으로 구분하여 입력
array = list(map(int, input().split()))
array.sort()     # 이진 탐색 수행 전 사전에 정렬 수행


# M(손님이 확인 요청한 부품 개수) 입력
m = int(input())
# 손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
request = list(map(int, input().split()))


# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in request:
    result = binary_search(array, i, 0, n-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')
