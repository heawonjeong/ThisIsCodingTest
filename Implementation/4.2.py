n=int(input())
N = n + 1
num = 0

for i in range(N):
    
    for j in range(60):
        for k in range(60):
            if '3' in  str(i)+str(j)+str(k):
                num += 1

print(num)