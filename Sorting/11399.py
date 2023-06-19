n = int(input())
peoples = list(map(int, input().split()))

peoples.sort()
answer = 0

for i in range(1, n+1):
    answer += sum(peoples[0:i])

print(answer)