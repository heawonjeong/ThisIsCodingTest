## 실전문제 큰수의법칙
# 여기서 큰수의 법칙은 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여
# 가장 큰 수를 만드는 법칙이다. 

# n, m, k를 공백으로 입력받기
n, m, k = map(int, input().split())

data = list(map(int, input().split()))
data.sort()
first = data[-1]
second = data[-2]

count = m // (k+1)
res = m % (k+1)
answer = count * k * first + res*first + count * second
print(answer) 
