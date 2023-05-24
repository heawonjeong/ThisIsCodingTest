location = input()

row=int(location[1])
column=location[0]

a=0
b=0

if row>=3 and row<=6:
    a=1

if str(column)=='c' or str(column)=='d' or str(column)=='e' or str(column)=='f':
    b=1

sum = a+b

if sum==2:
    way=8
elif sum==1:
    way=4
else:
    way=2
print(way)