'''
어떠한 수 N이 1이 될때까지 다음의 두 과정중 하나를 반복적으로 수행합니다.
1. N에서 1을 뺀다.
2. N을 K로 나눈다. (나누어떨어지면)
'''

n, k = map(int, input().split())
count = 0
while True:
    if n==1:
        break
    if n%k==0:
        n=n/k
        count += 1
    else:
        n = n - 1
        count +=1

print(count)