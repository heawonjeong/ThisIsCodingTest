# 떡의 개수 n, 떡 총 길이 m
n, m = map(int, input().split())

array = list(map(int, input().split()))

start = 0
end = max(array)

# 이진탐색 수행
result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        # 잘랐을 때 떡의 양 계산
        if x > mid:
            total += x - mid

    # 떡의 양이 부족한 경우 왼쪽 탐색
    if total < m:
        end = mid - 1
    # 떡의 양이 많은 경우 오른쪽 탐색
    else:
        result = mid
        start = mid + 1
print(result)



