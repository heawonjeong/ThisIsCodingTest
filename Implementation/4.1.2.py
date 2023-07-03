## 상하좌우
'''
N x N 정사각형 공간위
시작좌표는 왼쪽 위 (1,1)
L : 왼쪽으로 한칸이동
R : 오른쪽으로 한칸이동
U : 위로 한칸이동
D : 아래로 한칸이동
정사각형 공간밖은 무시 
'''

n =int(input())

plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
x, y = 1, 1
move_plan = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(4):
        if move_plan[i] == plan:
            nx = x + dx[i]
            ny = y + dy[i]
    
    if nx > n or nx <1 or ny > n or ny < 1:
        continue
    x, y = nx, ny    
print(x, y) 