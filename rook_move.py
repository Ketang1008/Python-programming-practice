column1 = int(input())
column2 = int(input())
row1= int(input())
row2 =int(input())
if row1 == column1 or row2 == column2:
    print('YES')
else:
    print('NO')




n = int(input())
m = int(input())
k = int(input())
if (k%n==0 or k%m==0) and (k/n<=m or k/m<=n):
    print('YES')
else :
    print('NO')


a = int(input())
b = int(input())
c = int(input())
if (c%a==0 or c%b==0) and (c/a<=b or c/b<=a):
    print('YES')
else :
    print('NO')
