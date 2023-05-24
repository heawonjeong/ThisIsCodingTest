n, k = map(int, input().split())
num = 0
r=n%k
while n>=k:
  n=n//k
  num +=1
  if n==1:
    break
print(num)