## 왕실의 나이트

'''
체스판 8 x 8
나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램
'''

input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

move_plans = [(1,2), (-1, 2), (1, -2), (-1, -2), (2,1), (-2, 1), (2, -1), (-2,-1)]
count = 0

for plan in move_plans:
    new_row = row + plan[0]
    new_colum = column + plan[1]
    if new_row >=1 and new_row <= 8 and new_colum >=1 and new_colum <=8:
        count += 1
print(count)